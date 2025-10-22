# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11l11ll_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1llllllllll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1l1l1lll111_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll111l1l_opy_ import bstack1l1ll11l11l_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111llll_opy_ import bstack1l1ll11111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll11llll_opy_ import bstack1llll1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll1lll1_opy_ import bstack1ll1ll1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll11l_opy_ import bstack1llll1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111lll1_opy_ import bstack1l1l111l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111111_opy_ import bstack1l1l111111_opy_, Events, bstack1lll1l1111_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l11l1l1l_opy_ import bstack1l11llll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1lllllll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import bstack1lll111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1lll1llllll_opy_
from bstack_utils.helper import Notset, bstack1l1l1ll1111_opy_, get_cli_dir, bstack1l11ll111ll_opy_, bstack111lllll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll1l1l1ll1_opy_ import bstack1ll11llll11_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1111ll_opy_ import bstack1111llllll_opy_
from bstack_utils.helper import Notset, bstack1l1l1ll1111_opy_, get_cli_dir, bstack1l11ll111ll_opy_, bstack111lllll1_opy_, bstack11lll11l11_opy_, bstack11l1l1lll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1llll_opy_, bstack1lll1l1ll11_opy_, bstack1lll11lll1l_opy_, bstack1ll1l1111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import bstack1llll11l1ll_opy_, bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_
from bstack_utils.constants import *
from bstack_utils.bstack11l1ll11ll_opy_ import bstack1l11l1111_opy_
from bstack_utils import bstack111l11ll1l_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11ll11111l_opy_, bstack111l1lllll_opy_
logger = bstack111l11ll1l_opy_.get_logger(__name__, bstack111l11ll1l_opy_.bstack1l1l1l11l11_opy_())
def bstack1l1l1llllll_opy_(bs_config):
    bstack1l1l11ll11l_opy_ = None
    bstack1l1l111ll11_opy_ = None
    try:
        bstack1l1l111ll11_opy_ = get_cli_dir()
        bstack1l1l11ll11l_opy_ = bstack1l11ll111ll_opy_(bstack1l1l111ll11_opy_)
        bstack1l11lllllll_opy_ = bstack1l1l1ll1111_opy_(bstack1l1l11ll11l_opy_, bstack1l1l111ll11_opy_, bs_config)
        bstack1l1l11ll11l_opy_ = bstack1l11lllllll_opy_ if bstack1l11lllllll_opy_ else bstack1l1l11ll11l_opy_
        if not bstack1l1l11ll11l_opy_:
            raise ValueError(bstack11l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠣጅ"))
    except Exception as ex:
        logger.debug(bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡲࡡࡵࡧࡶࡸࠥࡨࡩ࡯ࡣࡵࡽࠥࢁࡽࠣጆ").format(ex))
        bstack1l1l11ll11l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠤጇ"))
        if bstack1l1l11ll11l_opy_:
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠥ࡬ࡲࡰ࡯ࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴ࠻ࠢࠥገ") + str(bstack1l1l11ll11l_opy_) + bstack11l1l11_opy_ (u"ࠣࠤጉ"))
        else:
            logger.debug(bstack11l1l11_opy_ (u"ࠤࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺ࠻ࠡࡵࡨࡸࡺࡶࠠ࡮ࡣࡼࠤࡧ࡫ࠠࡪࡰࡦࡳࡲࡶ࡬ࡦࡶࡨ࠲ࠧጊ"))
    return bstack1l1l11ll11l_opy_, bstack1l1l111ll11_opy_
bstack1l11llllll1_opy_ = bstack11l1l11_opy_ (u"ࠥ࠽࠾࠿࠹ࠣጋ")
bstack1l11ll1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠦࡷ࡫ࡡࡥࡻࠥጌ")
bstack1l1l1llll11_opy_ = bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤግ")
bstack1l1l1lll1ll_opy_ = bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡌࡊࡕࡗࡉࡓࡥࡁࡅࡆࡕࠦጎ")
bstack11ll11l11l_opy_ = bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠥጏ")
bstack1l1l11l11ll_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡳࠤࠫࡃ࡮࠯࠮ࠫࠪࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡽࡄࡖ࠭࠳࠰ࠢጐ"))
bstack1l11llll1ll_opy_ = bstack11l1l11_opy_ (u"ࠤࡧࡩࡻ࡫࡬ࡰࡲࡰࡩࡳࡺࠢ጑")
bstack1l11lll11l1_opy_ = bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡓࡗࡉࡅࡠࡈࡄࡐࡑࡈࡁࡄࡍࠥጒ")
bstack1l1l1l1l11l_opy_ = [
    Events.bstack111lll1ll1_opy_,
    Events.CONNECT,
    Events.bstack1111l11lll_opy_,
]
class SDKCLI:
    _1ll1ll11111_opy_ = None
    process: Union[None, Any]
    bstack1l11ll1ll1l_opy_: bool
    bstack1l1l11l1ll1_opy_: bool
    bstack1l1l111ll1l_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l11llll11l_opy_: Union[None, grpc.Channel]
    bstack1l1l1l11l1l_opy_: str
    test_framework: TestFramework
    bstack1lllll1l1ll_opy_: bstack1lll111ll11_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l1llll1l_opy_: bstack1l1l111l1l1_opy_
    accessibility: bstack1l1l1lll111_opy_
    bstack111l1111ll_opy_: bstack1111llllll_opy_
    ai: bstack1l1ll11l11l_opy_
    bstack1l1l1lll11l_opy_: bstack1l1ll11111l_opy_
    bstack1l11lll1lll_opy_: List[bstack1llllllllll_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l11llll1_opy_: Any
    bstack1l11lll1ll1_opy_: Dict[str, timedelta]
    bstack1l11lll1111_opy_: str
    bstack1lll11l11ll_opy_: bstack1lll11l11l1_opy_
    def __new__(cls):
        if not cls._1ll1ll11111_opy_:
            cls._1ll1ll11111_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll11111_opy_
    def __init__(self):
        self.process = None
        self.bstack1l11ll1ll1l_opy_ = False
        self.bstack1l11llll11l_opy_ = None
        self.bstack1llllllll11_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l1lll1ll_opy_, None)
        self.bstack1l1l11l111l_opy_ = os.environ.get(bstack1l1l1llll11_opy_, bstack11l1l11_opy_ (u"ࠦࠧጓ")) == bstack11l1l11_opy_ (u"ࠧࠨጔ")
        self.bstack1l1l11l1ll1_opy_ = False
        self.bstack1l1l111ll1l_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l11llll1_opy_ = None
        self.test_framework = None
        self.bstack1lllll1l1ll_opy_ = None
        self.bstack1l1l1l11l1l_opy_=bstack11l1l11_opy_ (u"ࠨࠢጕ")
        self.session_framework = None
        self.logger = bstack111l11ll1l_opy_.get_logger(self.__class__.__name__, bstack111l11ll1l_opy_.bstack1l1l1l11l11_opy_())
        self.bstack1l11lll1ll1_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11l11ll_opy_ = bstack1lll11l11l1_opy_()
        self.bstack1l1l11111l1_opy_ = None
        self.bstack1ll1lll1111_opy_ = None
        self.bstack1l1l1llll1l_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l11lll1lll_opy_ = []
    def bstack1l11lllll1_opy_(self):
        return os.environ.get(bstack11ll11l11l_opy_).lower().__eq__(bstack11l1l11_opy_ (u"ࠢࡵࡴࡸࡩࠧ጖"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l11lll11l1_opy_, bstack11l1l11_opy_ (u"ࠨࠩ጗")).lower() in [bstack11l1l11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧጘ"), bstack11l1l11_opy_ (u"ࠪ࠵ࠬጙ"), bstack11l1l11_opy_ (u"ࠫࡾ࡫ࡳࠨጚ")]:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡌ࡯ࡳࡥ࡬ࡲ࡬ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡ࡯ࡲࡨࡪࠦࡤࡶࡧࠣࡸࡴࠦࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡏࡓࡅࡈࡣࡋࡇࡌࡍࡄࡄࡇࡐࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷࠤࡻࡧࡲࡪࡣࡥࡰࡪࠨጛ"))
            os.environ[bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤጜ")] = bstack11l1l11_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨጝ")
            return False
        if bstack11l1l11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬጞ") in config and str(config[bstack11l1l11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ጟ")]).lower() != bstack11l1l11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩጠ"):
            return False
        bstack1l1l11ll111_opy_ = [bstack11l1l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦጡ"), bstack11l1l11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤጢ")]
        bstack1l1l1111l11_opy_ = config.get(bstack11l1l11_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤጣ")) in bstack1l1l11ll111_opy_ or os.environ.get(bstack11l1l11_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨጤ")) in bstack1l1l11ll111_opy_
        os.environ[bstack11l1l11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦጥ")] = str(bstack1l1l1111l11_opy_) # bstack1l1l11l1lll_opy_ bstack1l1l1l111ll_opy_ VAR to bstack1l1l11lll1l_opy_ is binary running
        return bstack1l1l1111l11_opy_
    def bstack1l1ll1lll_opy_(self):
        for event in bstack1l1l1l1l11l_opy_:
            bstack1l1l111111_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l1l111111_opy_.logger.debug(bstack11l1l11_opy_ (u"ࠤࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠡ࠿ࡁࠤࢀࡧࡲࡨࡵࢀࠤࠧጦ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠥࠦጧ"))
            )
        bstack1l1l111111_opy_.register(Events.bstack111lll1ll1_opy_, self.__1l11ll1llll_opy_)
        bstack1l1l111111_opy_.register(Events.CONNECT, self.__1l1l111l1ll_opy_)
        bstack1l1l111111_opy_.register(Events.bstack1111l11lll_opy_, self.__1l11ll1ll11_opy_)
        bstack1l1l111111_opy_.register(Events.bstack1l1111111l_opy_, self.__1l11lllll1l_opy_)
    def bstack11ll111l1l_opy_(self):
        return not self.bstack1l1l11l111l_opy_ and os.environ.get(bstack1l1l1llll11_opy_, bstack11l1l11_opy_ (u"ࠦࠧጨ")) != bstack11l1l11_opy_ (u"ࠧࠨጩ")
    def is_running(self):
        if self.bstack1l1l11l111l_opy_:
            return self.bstack1l11ll1ll1l_opy_
        else:
            return bool(self.bstack1l11llll11l_opy_)
    def bstack1l1l111l111_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l11lll1lll_opy_) and cli.is_running()
    def __1l1l11l1l11_opy_(self, bstack1l1l1111ll1_opy_=10):
        if self.bstack1llllllll11_opy_:
            return
        bstack1ll1111ll_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l1lll1ll_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡛ࠣጪ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠢ࡞ࠢࡦࡳࡳࡴࡥࡤࡶ࡬ࡲ࡬ࠨጫ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11l1l11_opy_ (u"ࠣࡩࡵࡴࡨ࠴ࡥ࡯ࡣࡥࡰࡪࡥࡨࡵࡶࡳࡣࡵࡸ࡯ࡹࡻࠥጬ"), 0), (bstack11l1l11_opy_ (u"ࠤࡪࡶࡵࡩ࠮ࡦࡰࡤࡦࡱ࡫࡟ࡩࡶࡷࡴࡸࡥࡰࡳࡱࡻࡽࠧጭ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l1111ll1_opy_)
        self.bstack1l11llll11l_opy_ = channel
        self.bstack1llllllll11_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l11llll11l_opy_)
        self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࠤጮ"), datetime.now() - bstack1ll1111ll_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l1lll1ll_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࡀࠠࡪࡵࡢࡧ࡭࡯࡬ࡥࡡࡳࡶࡴࡩࡥࡴࡵࡀࠦጯ") + str(self.bstack11ll111l1l_opy_()) + bstack11l1l11_opy_ (u"ࠧࠨጰ"))
    def __1l11ll1ll11_opy_(self, event_name):
        if self.bstack11ll111l1l_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡲࡴࡵ࡯࡮ࡨࠢࡆࡐࡎࠨጱ"))
        self.__1l1l1ll111l_opy_()
    def __1l11lllll1l_opy_(self, event_name, bstack1l1l1l11ll1_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack11l1l11_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠢጲ"))
        bstack1l11lll11ll_opy_ = Path(bstack1lll11ll111_opy_ (u"ࠣࡽࡶࡩࡱ࡬࠮ࡤ࡮࡬ࡣࡩ࡯ࡲࡾ࠱ࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࡶ࠲࡯ࡹ࡯࡯ࠤጳ"))
        if self.bstack1l1l111ll11_opy_ and bstack1l11lll11ll_opy_.exists():
            with open(bstack1l11lll11ll_opy_, bstack11l1l11_opy_ (u"ࠩࡵࠫጴ"), encoding=bstack11l1l11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩጵ")) as fp:
                data = json.load(fp)
                try:
                    bstack11lll11l11_opy_(bstack11l1l11_opy_ (u"ࠫࡕࡕࡓࡕࠩጶ"), bstack1l11l1111_opy_(bstack1l1l1l1ll_opy_), data, {
                        bstack11l1l11_opy_ (u"ࠬࡧࡵࡵࡪࠪጷ"): (self.config[bstack11l1l11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨጸ")], self.config[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪጹ")])
                    })
                except Exception as e:
                    logger.debug(bstack111l1lllll_opy_.format(str(e)))
            bstack1l11lll11ll_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l1l1ll1l_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1l11ll1llll_opy_(self, event_name: str, data):
        from bstack_utils.bstack1111ll11ll_opy_ import bstack1llllll1ll1_opy_
        self.bstack1l1l1l11l1l_opy_, self.bstack1l1l111ll11_opy_ = bstack1l1l1llllll_opy_(data.bs_config)
        os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡘࡔࡌࡘࡆࡈࡌࡆࡡࡇࡍࡗ࠭ጺ")] = self.bstack1l1l111ll11_opy_
        if not self.bstack1l1l1l11l1l_opy_ or not self.bstack1l1l111ll11_opy_:
            raise ValueError(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸ࡭࡫ࠠࡔࡆࡎࠤࡈࡒࡉࠡࡤ࡬ࡲࡦࡸࡹࠣጻ"))
        if self.bstack11ll111l1l_opy_():
            self.__1l1l111l1ll_opy_(event_name, bstack1lll1l1111_opy_())
            return
        try:
            bstack1llllll1ll1_opy_.end(EVENTS.bstack11111ll1l_opy_.value, EVENTS.bstack11111ll1l_opy_.value + bstack11l1l11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥጼ"), EVENTS.bstack11111ll1l_opy_.value + bstack11l1l11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤጽ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࠠࡔࡆࡎࠤࡘ࡫ࡴࡶࡲ࠱ࠦጾ"))
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡼࡿࠥጿ").format(e))
        start = datetime.now()
        is_started = self.__1l1l11l11l1_opy_()
        self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠢࡴࡲࡤࡻࡳࡥࡴࡪ࡯ࡨࠦፀ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l11l1l11_opy_()
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢፁ"), datetime.now() - start)
            start = datetime.now()
            self.__1l11ll11ll1_opy_(data)
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢፂ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l11lll11_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1l1l111l1ll_opy_(self, event_name: str, data: bstack1lll1l1111_opy_):
        if not self.bstack11ll111l1l_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰࡰࡱࡩࡨࡺ࠺ࠡࡰࡲࡸࠥࡧࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢፃ"))
            return
        bin_session_id = os.environ.get(bstack1l1l1llll11_opy_)
        start = datetime.now()
        self.__1l1l11l1l11_opy_()
        self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥፄ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠡࡶࡲࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡃࡍࡋࠣࠦፅ") + str(bin_session_id) + bstack11l1l11_opy_ (u"ࠨࠢፆ"))
        start = datetime.now()
        self.__1l1l1111lll_opy_()
        self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧፇ"), datetime.now() - start)
    def __1l11lll1l1l_opy_(self):
        if not self.bstack1llllllll11_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡥࡤࡲࡳࡵࡴࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࠤࡲࡵࡤࡶ࡮ࡨࡷࠧፈ"))
            return
        bstack1l1ll111111_opy_ = {
            bstack11l1l11_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨፉ"): (bstack1ll1ll1ll11_opy_, bstack1llll1111ll_opy_, bstack1lll1llllll_opy_),
            bstack11l1l11_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧፊ"): (bstack1llll1l1ll1_opy_, bstack1lll111lll1_opy_, bstack1lllllll11l_opy_),
        }
        if not self.bstack1l1l11111l1_opy_ and self.session_framework in bstack1l1ll111111_opy_:
            bstack1l1l1111l1l_opy_, bstack1l11ll1l1ll_opy_, bstack1l11lll111l_opy_ = bstack1l1ll111111_opy_[self.session_framework]
            bstack1l1l1l1l1ll_opy_ = bstack1l11ll1l1ll_opy_()
            self.bstack1ll1lll1111_opy_ = bstack1l1l1l1l1ll_opy_
            self.bstack1l1l11111l1_opy_ = bstack1l11lll111l_opy_
            self.bstack1l11lll1lll_opy_.append(bstack1l1l1l1l1ll_opy_)
            self.bstack1l11lll1lll_opy_.append(bstack1l1l1111l1l_opy_(self.bstack1ll1lll1111_opy_))
        if not self.bstack1l1l1llll1l_opy_ and self.config_observability and self.config_observability.success: # bstack1llll11ll11_opy_
            self.bstack1l1l1llll1l_opy_ = bstack1l1l111l1l1_opy_(self.bstack1l1l11111l1_opy_, self.bstack1ll1lll1111_opy_) # bstack1l1l1lll1l1_opy_
            self.bstack1l11lll1lll_opy_.append(self.bstack1l1l1llll1l_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l1lll111_opy_(self.bstack1l1l11111l1_opy_, self.bstack1ll1lll1111_opy_)
            self.bstack1l11lll1lll_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11l1l11_opy_ (u"ࠦࡸ࡫࡬ࡧࡊࡨࡥࡱࠨፋ"), False) == True:
            self.ai = bstack1l1ll11l11l_opy_()
            self.bstack1l11lll1lll_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l11llll1_opy_ and self.bstack1l1l11llll1_opy_.success:
            self.percy = bstack1l1ll11111l_opy_(self.bstack1l1l11llll1_opy_)
            self.bstack1l11lll1lll_opy_.append(self.percy)
        for mod in self.bstack1l11lll1lll_opy_:
            if not mod.bstack1lll11l1l11_opy_():
                mod.configure(self.bstack1llllllll11_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11l11ll_opy_)
    def __1l11ll11l1l_opy_(self):
        for mod in self.bstack1l11lll1lll_opy_:
            if mod.bstack1lll11l1l11_opy_():
                mod.configure(self.bstack1llllllll11_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l1l111l11l_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1l11ll11ll1_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l11l1ll1_opy_:
            return
        self.__1l11lllll11_opy_(data)
        bstack1ll1111ll_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11l1l11_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧፌ")
        req.sdk_language = bstack11l1l11_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨፍ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l11l11ll_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࠤፎ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡷࡹࡧࡲࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢፏ"))
            r = self.bstack1llllllll11_opy_.StartBinSession(req)
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦፐ"), datetime.now() - bstack1ll1111ll_opy_)
            os.environ[bstack1l1l1llll11_opy_] = r.bin_session_id
            self.__1l1l1l1llll_opy_(r)
            self.__1l11lll1l1l_opy_()
            self.bstack1lll11l11ll_opy_.start()
            self.bstack1l1l11l1ll1_opy_ = True
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟ࠧፑ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠦࡢࠦ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠤፒ"))
        except grpc.bstack1l11lll1l11_opy_ as bstack1l11ll1l11l_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡹ࡯࡭ࡦࡱࡨࡹࡹ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢፓ") + str(bstack1l11ll1l11l_opy_) + bstack11l1l11_opy_ (u"ࠨࠢፔ"))
            traceback.print_exc()
            raise bstack1l11ll1l11l_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦፕ") + str(e) + bstack11l1l11_opy_ (u"ࠣࠤፖ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l1l1l111_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1l1l1111lll_opy_(self):
        if not self.bstack11ll111l1l_opy_() or not self.cli_bin_session_id or self.bstack1l1l111ll1l_opy_:
            return
        bstack1ll1111ll_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩፗ"), bstack11l1l11_opy_ (u"ࠪ࠴ࠬፘ")))
        try:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡠࠨፙ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢፚ"))
            r = self.bstack1llllllll11_opy_.ConnectBinSession(req)
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡨࡵ࡮࡯ࡧࡦࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥ፛"), datetime.now() - bstack1ll1111ll_opy_)
            self.__1l1l1l1llll_opy_(r)
            self.__1l11lll1l1l_opy_()
            self.bstack1lll11l11ll_opy_.start()
            self.bstack1l1l111ll1l_opy_ = True
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࠤ፜") + str(id(self)) + bstack11l1l11_opy_ (u"ࠣ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠢ፝"))
        except grpc.bstack1l11lll1l11_opy_ as bstack1l11ll1l11l_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦ፞") + str(bstack1l11ll1l11l_opy_) + bstack11l1l11_opy_ (u"ࠥࠦ፟"))
            traceback.print_exc()
            raise bstack1l11ll1l11l_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣ፠") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨ፡"))
            traceback.print_exc()
            raise e
    def __1l1l1l1llll_opy_(self, r):
        self.bstack1l1l11lllll_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11l1l11_opy_ (u"ࠨࡵ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡷࡪࡸࡶࡦࡴࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧ።") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11l1l11_opy_ (u"ࠢࡦ࡯ࡳࡸࡾࠦࡣࡰࡰࡩ࡭࡬ࠦࡦࡰࡷࡱࡨࠧ፣"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡥࡳࡥࡼࠤ࡮ࡹࠠࡴࡧࡱࡸࠥࡵ࡮࡭ࡻࠣࡥࡸࠦࡰࡢࡴࡷࠤࡴ࡬ࠠࡵࡪࡨࠤࠧࡉ࡯࡯ࡰࡨࡧࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠮ࠥࠤࡦࡴࡤࠡࡶ࡫࡭ࡸࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡦࡲࡳࡰࠢࡸࡷࡪࡪࠠࡣࡻࠣࡗࡹࡧࡲࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪࡨࡶࡪ࡬࡯ࡳࡧ࠯ࠤࡓࡵ࡮ࡦࠢ࡫ࡥࡳࡪ࡬ࡪࡰࡪࠤ࡮ࡹࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ፤")
        self.bstack1l1l11llll1_opy_ = getattr(r, bstack11l1l11_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ፥"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ፦")] = self.config_testhub.jwt
        os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ፧")] = self.config_testhub.build_hashed_id
    def bstack1l11ll1lll1_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l11ll1ll1l_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1ll1111l1_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1ll1111l1_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l11ll1lll1_opy_(event_name=EVENTS.bstack1l1l1l1ll11_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1l1l11l11l1_opy_(self, bstack1l1l1111ll1_opy_=10):
        if self.bstack1l11ll1ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡹࡴࡢࡴࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠢ፨"))
            return True
        self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧ፩"))
        if os.getenv(bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡉࡓ࡜ࠢ፪")) == bstack1l11llll1ll_opy_:
            self.cli_bin_session_id = bstack1l11llll1ll_opy_
            self.cli_listen_addr = bstack11l1l11_opy_ (u"ࠣࡷࡱ࡭ࡽࡀ࠯ࡵ࡯ࡳ࠳ࡸࡪ࡫࠮ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠰ࠩࡸ࠴ࡳࡰࡥ࡮ࠦ፫") % (self.cli_bin_session_id)
            self.bstack1l11ll1ll1l_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l1l11l1l_opy_, bstack11l1l11_opy_ (u"ࠤࡶࡨࡰࠨ፬")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1111111_opy_ compat for text=True in bstack1l1l1l111l1_opy_ python
            encoding=bstack11l1l11_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤ፭"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l11ll11l11_opy_ = threading.Thread(target=self.__1l1l1l1l1l1_opy_, args=(bstack1l1l1111ll1_opy_,))
        bstack1l11ll11l11_opy_.start()
        bstack1l11ll11l11_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡷࡵࡧࡷ࡯࠼ࠣࡶࡪࡺࡵࡳࡰࡦࡳࡩ࡫࠽ࡼࡵࡨࡰ࡫࠴ࡰࡳࡱࡦࡩࡸࡹ࠮ࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࢁࠥࡵࡵࡵ࠿ࡾࡷࡪࡲࡦ࠯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡶࡸࡩࡵࡵࡵ࠰ࡵࡩࡦࡪࠨࠪࡿࠣࡩࡷࡸ࠽ࠣ፮") + str(self.process.stderr.read()) + bstack11l1l11_opy_ (u"ࠧࠨ፯"))
        if not self.bstack1l11ll1ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡛ࠣ፰") + str(id(self)) + bstack11l1l11_opy_ (u"ࠢ࡞ࠢࡦࡰࡪࡧ࡮ࡶࡲࠥ፱"))
            self.__1l1l1ll111l_opy_()
        self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡱࡴࡲࡧࡪࡹࡳࡠࡴࡨࡥࡩࡿ࠺ࠡࠤ፲") + str(self.bstack1l11ll1ll1l_opy_) + bstack11l1l11_opy_ (u"ࠤࠥ፳"))
        return self.bstack1l11ll1ll1l_opy_
    def __1l1l1l1l1l1_opy_(self, bstack1l1l1ll11l1_opy_=10):
        bstack1l1l1ll1l11_opy_ = time.time()
        while self.process and time.time() - bstack1l1l1ll1l11_opy_ < bstack1l1l1ll11l1_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11l1l11_opy_ (u"ࠥ࡭ࡩࡃࠢ፴") in line:
                    self.cli_bin_session_id = line.split(bstack11l1l11_opy_ (u"ࠦ࡮ࡪ࠽ࠣ፵"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡩ࡬ࡪࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦ࠽ࠦ፶") + str(self.cli_bin_session_id) + bstack11l1l11_opy_ (u"ࠨࠢ፷"))
                    continue
                if bstack11l1l11_opy_ (u"ࠢ࡭࡫ࡶࡸࡪࡴ࠽ࠣ፸") in line:
                    self.cli_listen_addr = line.split(bstack11l1l11_opy_ (u"ࠣ࡮࡬ࡷࡹ࡫࡮࠾ࠤ፹"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡦࡰ࡮ࡥ࡬ࡪࡵࡷࡩࡳࡥࡡࡥࡦࡵ࠾ࠧ፺") + str(self.cli_listen_addr) + bstack11l1l11_opy_ (u"ࠥࠦ፻"))
                    continue
                if bstack11l1l11_opy_ (u"ࠦࡵࡵࡲࡵ࠿ࠥ፼") in line:
                    port = line.split(bstack11l1l11_opy_ (u"ࠧࡶ࡯ࡳࡶࡀࠦ፽"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡰࡰࡴࡷ࠾ࠧ፾") + str(port) + bstack11l1l11_opy_ (u"ࠢࠣ፿"))
                    continue
                if line.strip() == bstack1l11ll1l1l1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11l1l11_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡊࡑࡢࡗ࡙ࡘࡅࡂࡏࠥᎀ"), bstack11l1l11_opy_ (u"ࠤ࠴ࠦᎁ")) == bstack11l1l11_opy_ (u"ࠥ࠵ࠧᎂ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l11ll1ll1l_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡪࡸࡲࡰࡴ࠽ࠤࠧᎃ") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨᎄ"))
        return False
    @measure(event_name=EVENTS.bstack1l11ll1111l_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1l1l1ll111l_opy_(self):
        if self.bstack1l11llll11l_opy_:
            self.bstack1lll11l11ll_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l1l11111_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l111ll1l_opy_:
                    self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠨࡳࡵࡱࡳࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥᎅ"), datetime.now() - start)
                else:
                    self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠢࡴࡶࡲࡴࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦᎆ"), datetime.now() - start)
            self.__1l11ll11l1l_opy_()
            start = datetime.now()
            self.bstack1l11llll11l_opy_.close()
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠣࡦ࡬ࡷࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥᎇ"), datetime.now() - start)
            self.bstack1l11llll11l_opy_ = None
        if self.process:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡶࡸࡴࡶࠢᎈ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠥ࡯࡮ࡲ࡬ࡠࡶ࡬ࡱࡪࠨᎉ"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l11l111l_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1llll11l1l_opy_()
                self.logger.info(
                    bstack11l1l11_opy_ (u"࡛ࠦ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠦᎊ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᎋ")] = self.config_testhub.build_hashed_id
        self.bstack1l11ll1ll1l_opy_ = False
    def __1l11lllll11_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11l1l11_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᎌ")] = selenium.__version__
            data.frameworks.append(bstack11l1l11_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᎍ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᎎ")] = __version__
            data.frameworks.append(bstack11l1l11_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᎏ"))
        except:
            pass
    def bstack1l1l1ll1l1l_opy_(self, hub_url: str, platform_index: int, bstack1l1llll1l_opy_: Any):
        if self.bstack1lllll1l1ll_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠤࡸ࡫ࡴࡶࡲࠣࡷࡪࡲࡥ࡯࡫ࡸࡱ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡴࡧࡷࠤࡺࡶࠢ᎐"))
            return
        try:
            bstack1ll1111ll_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11l1l11_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ᎑")
            self.bstack1lllll1l1ll_opy_ = bstack1lllllll11l_opy_(
                cli.config.get(bstack11l1l11_opy_ (u"ࠧ࡮ࡵࡣࡗࡵࡰࠧ᎒"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll1l1111_opy_={bstack11l1l11_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥ᎓"): bstack1l1llll1l_opy_}
            )
            def bstack1l1l1lllll1_opy_(self):
                return
            if self.config.get(bstack11l1l11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠤ᎔"), True):
                Service.start = bstack1l1l1lllll1_opy_
                Service.stop = bstack1l1l1lllll1_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.upload_attachment = staticmethod(bstack1111llllll_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11llll11_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤ᎕"), datetime.now() - bstack1ll1111ll_opy_)
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡀࠠࠣ᎖") + str(e) + bstack11l1l11_opy_ (u"ࠥࠦ᎗"))
    def bstack1l1l1l1111l_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1ll1l1l1l_opy_
            self.bstack1lllll1l1ll_opy_ = bstack1lll1llllll_opy_(
                platform_index,
                framework_name=bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ᎘"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠾ࠥࠨ᎙") + str(e) + bstack11l1l11_opy_ (u"ࠨࠢ᎚"))
            pass
    def bstack1l1l11111ll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡶࡩࡹࠦࡵࡱࠤ᎛"))
            return
        if bstack111lllll1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣ᎜"): pytest.__version__ }, [bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨ᎝")], self.bstack1lll11l11ll_opy_, self.bstack1llllllll11_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l11llll1l1_opy_({ bstack11l1l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ᎞"): pytest.__version__ }, [bstack11l1l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦ᎟")], self.bstack1lll11l11ll_opy_, self.bstack1llllllll11_opy_)
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࠤᎠ") + str(e) + bstack11l1l11_opy_ (u"ࠨࠢᎡ"))
        self.bstack1l1l1l1lll1_opy_()
    def bstack1l1l1l1lll1_opy_(self):
        if not self.bstack1l11lllll1_opy_():
            return
        bstack111l1lll11_opy_ = None
        def bstack1ll1111lll_opy_(config, startdir):
            return bstack11l1l11_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧᎢ").format(bstack11l1l11_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢᎣ"))
        def bstack11ll1l1ll1_opy_():
            return
        def bstack11ll1111l_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11l1l11_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩᎤ"):
                return bstack11l1l11_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤᎥ")
            else:
                return bstack111l1lll11_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack111l1lll11_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1ll1111lll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11ll1l1ll1_opy_
            Config.getoption = bstack11ll1111l_opy_
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡷࡧ࡭ࠦࡰࡺࡶࡨࡷࡹࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡨࡲࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠾ࠥࠨᎦ") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨᎧ"))
    def bstack1l1l1ll1lll_opy_(self):
        bstack111lll1l11_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack111lll1l11_opy_, dict):
            if cli.config_observability:
                bstack111lll1l11_opy_.update(
                    {bstack11l1l11_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨᎨ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11l1l11_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡡࡷࡳࡤࡽࡲࡢࡲࠥᎩ") in accessibility.get(bstack11l1l11_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᎪ"), {}):
                    bstack1l1l11l1111_opy_ = accessibility.get(bstack11l1l11_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᎫ"))
                    bstack1l1l11l1111_opy_.update({ bstack11l1l11_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷ࡙ࡵࡗࡳࡣࡳࠦᎬ"): bstack1l1l11l1111_opy_.pop(bstack11l1l11_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢᎭ")) })
                bstack111lll1l11_opy_.update({bstack11l1l11_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧᎮ"): accessibility })
        return bstack111lll1l11_opy_
    @measure(event_name=EVENTS.bstack1l1l1ll1ll1_opy_, stage=STAGE.bstack111llllll_opy_)
    def bstack1l1l1l11111_opy_(self, bstack1l1l1l11lll_opy_: str = None, bstack1l11ll111l1_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1llllllll11_opy_:
            return
        bstack1ll1111ll_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1l11lll_opy_:
            req.bstack1l1l1l11lll_opy_ = bstack1l1l1l11lll_opy_
        if bstack1l11ll111l1_opy_:
            req.bstack1l11ll111l1_opy_ = bstack1l11ll111l1_opy_
        try:
            r = self.bstack1llllllll11_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺ࡯ࡱࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᎯ"), datetime.now() - bstack1ll1111ll_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack111lllllll_opy_(self, key: str, value: timedelta):
        tag = bstack11l1l11_opy_ (u"ࠢࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢᎰ") if self.bstack11ll111l1l_opy_() else bstack11l1l11_opy_ (u"ࠣ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹࠢᎱ")
        self.bstack1l11lll1ll1_opy_[bstack11l1l11_opy_ (u"ࠤ࠽ࠦᎲ").join([tag + bstack11l1l11_opy_ (u"ࠥ࠱ࠧᎳ") + str(id(self)), key])] += value
    def bstack1llll11l1l_opy_(self):
        if not os.getenv(bstack11l1l11_opy_ (u"ࠦࡉࡋࡂࡖࡉࡢࡔࡊࡘࡆࠣᎴ"), bstack11l1l11_opy_ (u"ࠧ࠶ࠢᎵ")) == bstack11l1l11_opy_ (u"ࠨ࠱ࠣᎶ"):
            return
        bstack1l1l11ll1ll_opy_ = dict()
        bstack1lll1lll1ll_opy_ = []
        if self.test_framework:
            bstack1lll1lll1ll_opy_.extend(list(self.test_framework.bstack1lll1lll1ll_opy_.values()))
        if self.bstack1lllll1l1ll_opy_:
            bstack1lll1lll1ll_opy_.extend(list(self.bstack1lllll1l1ll_opy_.bstack1lll1lll1ll_opy_.values()))
        for instance in bstack1lll1lll1ll_opy_:
            if not instance.platform_index in bstack1l1l11ll1ll_opy_:
                bstack1l1l11ll1ll_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l11ll1ll_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll11l1l_opy_().items():
                report[k] += v
                report[k.split(bstack11l1l11_opy_ (u"ࠢ࠻ࠤᎷ"))[0]] += v
        bstack1l11llll111_opy_ = sorted([(k, v) for k, v in self.bstack1l11lll1ll1_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l111111l_opy_ = 0
        for r in bstack1l11llll111_opy_:
            bstack1l11ll1l111_opy_ = r[1].total_seconds()
            bstack1l1l111111l_opy_ += bstack1l11ll1l111_opy_
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࢁࡲ࡜࠲ࡠࢁࡂࠨᎸ") + str(bstack1l11ll1l111_opy_) + bstack11l1l11_opy_ (u"ࠤࠥᎹ"))
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࠱࠲ࠨᎺ"))
        bstack1l1l1ll11ll_opy_ = []
        for platform_index, report in bstack1l1l11ll1ll_opy_.items():
            bstack1l1l1ll11ll_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l1ll11ll_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1ll1lll1l_opy_ = set()
        bstack1l1l11ll1l1_opy_ = 0
        for r in bstack1l1l1ll11ll_opy_:
            bstack1l11ll1l111_opy_ = r[2].total_seconds()
            bstack1l1l11ll1l1_opy_ += bstack1l11ll1l111_opy_
            bstack1ll1lll1l_opy_.add(r[0])
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡹ࡫ࡳࡵ࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࠱ࢀࡸ࡛࠱࡟ࢀ࠾ࢀࡸ࡛࠲࡟ࢀࡁࠧᎻ") + str(bstack1l11ll1l111_opy_) + bstack11l1l11_opy_ (u"ࠧࠨᎼ"))
        if self.bstack11ll111l1l_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࠭࠮ࠤᎽ"))
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࡁࢀࡺ࡯ࡵࡣ࡯ࡣࡨࡲࡩࡾࠢࡷࡩࡸࡺ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ࠰ࡿࡸࡺࡲࠩࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ࠭ࢂࡃࠢᎾ") + str(bstack1l1l11ll1l1_opy_) + bstack11l1l11_opy_ (u"ࠣࠤᎿ"))
        else:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷࡂࠨᏀ") + str(bstack1l1l111111l_opy_) + bstack11l1l11_opy_ (u"ࠥࠦᏁ"))
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦ࠲࠳ࠢᏂ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1llllllll11_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧࡩ࡬ࡪࡡࡶࡩࡷࡼࡩࡤࡧࠣ࡭ࡸࠦ࡮ࡰࡶࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࡤ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤᏃ"))
            return None
        response = self.bstack1llllllll11_opy_.TestOrchestration(request)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷ࠱ࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠱ࡸ࡫ࡳࡴ࡫ࡲࡲࡂࢁࡽࠣᏄ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l11lllll_opy_(self, r):
        if r is not None and getattr(r, bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࠨᏅ"), None) and getattr(r.testhub, bstack11l1l11_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨᏆ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11l1l11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᏇ")))
            for bstack1l11ll11lll_opy_, err in errors.items():
                if err[bstack11l1l11_opy_ (u"ࠪࡸࡾࡶࡥࠨᏈ")] == bstack11l1l11_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᏉ"):
                    self.logger.info(err[bstack11l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ꮚ")])
                else:
                    self.logger.error(err[bstack11l1l11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᏋ")])
    def bstack11111l111l_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()