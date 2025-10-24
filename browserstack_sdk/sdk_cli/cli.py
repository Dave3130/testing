# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11l1ll1_opy_ import bstack1lll11ll111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1llll_opy_ import bstack1l1l1llll1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll11l111_opy_ import bstack1l1ll1l111l_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111ll11_opy_ import bstack1l1l111ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll11ll_opy_ import bstack1ll1lll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1ll_opy_ import bstack1lll1ll1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1l11l1l_opy_ import bstack1l11lll1111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll_opy_ import bstack1llllll1ll_opy_, Events, bstack11llll111l_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l11lll1ll1_opy_ import bstack1l11ll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1111111l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import bstack1lll11111ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1ll11_opy_ import bstack1llll111l11_opy_
from bstack_utils.helper import Notset, bstack1l1l11111l1_opy_, get_cli_dir, bstack1l1l1ll1lll_opy_, bstack1l11l11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll111ll11l_opy_ import bstack1ll11llllll_opy_
from browserstack_sdk.sdk_cli.utils.bstack111llll11l_opy_ import bstack1111lll1l_opy_
from bstack_utils.helper import Notset, bstack1l1l11111l1_opy_, get_cli_dir, bstack1l1l1ll1lll_opy_, bstack1l11l11ll_opy_, bstack1lll1l1l11_opy_, bstack1l11lll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l11l_opy_, bstack1lll1l11111_opy_, bstack1lll11llll1_opy_, bstack1ll111ll111_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import bstack1llllll1l1l_opy_, bstack1llllll111l_opy_, bstack1llll1l111l_opy_
from bstack_utils.constants import *
from bstack_utils.bstack11l11l111l_opy_ import bstack11ll1ll1ll_opy_
from bstack_utils import bstack1ll1111l1_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1ll1lllll1_opy_, bstack11ll11l1ll_opy_
logger = bstack1ll1111l1_opy_.get_logger(__name__, bstack1ll1111l1_opy_.bstack1l1l111l1ll_opy_())
def bstack1l1l1lllll1_opy_(bs_config):
    bstack1l1ll1111ll_opy_ = None
    bstack1l1l1ll1l11_opy_ = None
    try:
        bstack1l1l1ll1l11_opy_ = get_cli_dir()
        bstack1l1ll1111ll_opy_ = bstack1l1l1ll1lll_opy_(bstack1l1l1ll1l11_opy_)
        bstack1l1l1l1l111_opy_ = bstack1l1l11111l1_opy_(bstack1l1ll1111ll_opy_, bstack1l1l1ll1l11_opy_, bs_config)
        bstack1l1ll1111ll_opy_ = bstack1l1l1l1l111_opy_ if bstack1l1l1l1l111_opy_ else bstack1l1ll1111ll_opy_
        if not bstack1l1ll1111ll_opy_:
            raise ValueError(bstack1l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠣዾ"))
    except Exception as ex:
        logger.debug(bstack1l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡲࡡࡵࡧࡶࡸࠥࡨࡩ࡯ࡣࡵࡽࠥࢁࡽࠣዿ").format(ex))
        bstack1l1ll1111ll_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠤጀ"))
        if bstack1l1ll1111ll_opy_:
            logger.debug(bstack1l1_opy_ (u"ࠢࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠥ࡬ࡲࡰ࡯ࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴ࠻ࠢࠥጁ") + str(bstack1l1ll1111ll_opy_) + bstack1l1_opy_ (u"ࠣࠤጂ"))
        else:
            logger.debug(bstack1l1_opy_ (u"ࠤࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺ࠻ࠡࡵࡨࡸࡺࡶࠠ࡮ࡣࡼࠤࡧ࡫ࠠࡪࡰࡦࡳࡲࡶ࡬ࡦࡶࡨ࠲ࠧጃ"))
    return bstack1l1ll1111ll_opy_, bstack1l1l1ll1l11_opy_
bstack1l1l111l1l1_opy_ = bstack1l1_opy_ (u"ࠥ࠽࠾࠿࠹ࠣጄ")
bstack1l1l11l1l1l_opy_ = bstack1l1_opy_ (u"ࠦࡷ࡫ࡡࡥࡻࠥጅ")
bstack1l11llll111_opy_ = bstack1l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤጆ")
bstack1l1l1l1111l_opy_ = bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡌࡊࡕࡗࡉࡓࡥࡁࡅࡆࡕࠦጇ")
bstack1ll11ll1ll_opy_ = bstack1l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠥገ")
bstack1l1l11l1l11_opy_ = re.compile(bstack1l1_opy_ (u"ࡳࠤࠫࡃ࡮࠯࠮ࠫࠪࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡽࡄࡖ࠭࠳࠰ࠢጉ"))
bstack1l11llll11l_opy_ = bstack1l1_opy_ (u"ࠤࡧࡩࡻ࡫࡬ࡰࡲࡰࡩࡳࡺࠢጊ")
bstack1l1l1l111l1_opy_ = bstack1l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡓࡗࡉࡅࡠࡈࡄࡐࡑࡈࡁࡄࡍࠥጋ")
bstack1l11llll1ll_opy_ = [
    Events.bstack1ll1111111_opy_,
    Events.CONNECT,
    Events.bstack111l1l11l_opy_,
]
class SDKCLI:
    _1ll1ll11l1l_opy_ = None
    process: Union[None, Any]
    bstack1l1ll111111_opy_: bool
    bstack1l11llllll1_opy_: bool
    bstack1l11ll1ll1l_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1ll11111l_opy_: Union[None, grpc.Channel]
    bstack1l1l11l1lll_opy_: str
    test_framework: TestFramework
    bstack1llll11ll1l_opy_: bstack1lll11111ll_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1ll111l1l_opy_: bstack1l11lll1111_opy_
    accessibility: bstack1l1l1llll1l_opy_
    bstack111llll11l_opy_: bstack1111lll1l_opy_
    ai: bstack1l1ll1l111l_opy_
    bstack1l1l1111l1l_opy_: bstack1l1l111ll1l_opy_
    bstack1l1l111l111_opy_: List[bstack1llll1llll1_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l1l11ll1_opy_: Any
    bstack1l1l1ll1111_opy_: Dict[str, timedelta]
    bstack1l1l11ll1ll_opy_: str
    bstack1lll11l1ll1_opy_: bstack1lll11ll111_opy_
    def __new__(cls):
        if not cls._1ll1ll11l1l_opy_:
            cls._1ll1ll11l1l_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll11l1l_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1ll111111_opy_ = False
        self.bstack1l1ll11111l_opy_ = None
        self.bstack1llll1l11ll_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l1l1111l_opy_, None)
        self.bstack1l1l11l1111_opy_ = os.environ.get(bstack1l11llll111_opy_, bstack1l1_opy_ (u"ࠦࠧጌ")) == bstack1l1_opy_ (u"ࠧࠨግ")
        self.bstack1l11llllll1_opy_ = False
        self.bstack1l11ll1ll1l_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l1l11ll1_opy_ = None
        self.test_framework = None
        self.bstack1llll11ll1l_opy_ = None
        self.bstack1l1l11l1lll_opy_=bstack1l1_opy_ (u"ࠨࠢጎ")
        self.session_framework = None
        self.logger = bstack1ll1111l1_opy_.get_logger(self.__class__.__name__, bstack1ll1111l1_opy_.bstack1l1l111l1ll_opy_())
        self.bstack1l1l1ll1111_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11l1ll1_opy_ = bstack1lll11ll111_opy_()
        self.bstack1l1l1llll11_opy_ = None
        self.bstack1ll1ll1llll_opy_ = None
        self.bstack1l1ll111l1l_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l111l111_opy_ = []
    def bstack1lllllll11_opy_(self):
        return os.environ.get(bstack1ll11ll1ll_opy_).lower().__eq__(bstack1l1_opy_ (u"ࠢࡵࡴࡸࡩࠧጏ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l1l111l1_opy_, bstack1l1_opy_ (u"ࠨࠩጐ")).lower() in [bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ጑"), bstack1l1_opy_ (u"ࠪ࠵ࠬጒ"), bstack1l1_opy_ (u"ࠫࡾ࡫ࡳࠨጓ")]:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡌ࡯ࡳࡥ࡬ࡲ࡬ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡ࡯ࡲࡨࡪࠦࡤࡶࡧࠣࡸࡴࠦࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡏࡓࡅࡈࡣࡋࡇࡌࡍࡄࡄࡇࡐࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷࠤࡻࡧࡲࡪࡣࡥࡰࡪࠨጔ"))
            os.environ[bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤጕ")] = bstack1l1_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨ጖")
            return False
        if bstack1l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ጗") in config and str(config[bstack1l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ጘ")]).lower() != bstack1l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩጙ"):
            return False
        bstack1l1l1l11l11_opy_ = [bstack1l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦጚ"), bstack1l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤጛ")]
        bstack1l1l1l1llll_opy_ = config.get(bstack1l1_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤጜ")) in bstack1l1l1l11l11_opy_ or os.environ.get(bstack1l1_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨጝ")) in bstack1l1l1l11l11_opy_
        os.environ[bstack1l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦጞ")] = str(bstack1l1l1l1llll_opy_) # bstack1l1l1llllll_opy_ bstack1l1l11ll1l1_opy_ VAR to bstack1l1l1l11lll_opy_ is binary running
        return bstack1l1l1l1llll_opy_
    def bstack1111l1ll1_opy_(self):
        for event in bstack1l11llll1ll_opy_:
            bstack1llllll1ll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1llllll1ll_opy_.logger.debug(bstack1l1_opy_ (u"ࠤࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠡ࠿ࡁࠤࢀࡧࡲࡨࡵࢀࠤࠧጟ") + str(kwargs) + bstack1l1_opy_ (u"ࠥࠦጠ"))
            )
        bstack1llllll1ll_opy_.register(Events.bstack1ll1111111_opy_, self.__1l1l1ll11l1_opy_)
        bstack1llllll1ll_opy_.register(Events.CONNECT, self.__1l11ll1l1l1_opy_)
        bstack1llllll1ll_opy_.register(Events.bstack111l1l11l_opy_, self.__1l11ll11ll1_opy_)
        bstack1llllll1ll_opy_.register(Events.bstack1l1ll11111_opy_, self.__1l1l1l1lll1_opy_)
    def bstack11l11l1l1l_opy_(self):
        return not self.bstack1l1l11l1111_opy_ and os.environ.get(bstack1l11llll111_opy_, bstack1l1_opy_ (u"ࠦࠧጡ")) != bstack1l1_opy_ (u"ࠧࠨጢ")
    def is_running(self):
        if self.bstack1l1l11l1111_opy_:
            return self.bstack1l1ll111111_opy_
        else:
            return bool(self.bstack1l1ll11111l_opy_)
    def bstack1l1l11l11l1_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l111l111_opy_) and cli.is_running()
    def __1l11lll1l11_opy_(self, bstack1l1ll111l11_opy_=10):
        if self.bstack1llll1l11ll_opy_:
            return
        bstack1l1ll111l_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l1l1111l_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1l1_opy_ (u"ࠨ࡛ࠣጣ") + str(id(self)) + bstack1l1_opy_ (u"ࠢ࡞ࠢࡦࡳࡳࡴࡥࡤࡶ࡬ࡲ࡬ࠨጤ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1l1_opy_ (u"ࠣࡩࡵࡴࡨ࠴ࡥ࡯ࡣࡥࡰࡪࡥࡨࡵࡶࡳࡣࡵࡸ࡯ࡹࡻࠥጥ"), 0), (bstack1l1_opy_ (u"ࠤࡪࡶࡵࡩ࠮ࡦࡰࡤࡦࡱ࡫࡟ࡩࡶࡷࡴࡸࡥࡰࡳࡱࡻࡽࠧጦ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1ll111l11_opy_)
        self.bstack1l1ll11111l_opy_ = channel
        self.bstack1llll1l11ll_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1ll11111l_opy_)
        self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࠤጧ"), datetime.now() - bstack1l1ll111l_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l1l1111l_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1l1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࡀࠠࡪࡵࡢࡧ࡭࡯࡬ࡥࡡࡳࡶࡴࡩࡥࡴࡵࡀࠦጨ") + str(self.bstack11l11l1l1l_opy_()) + bstack1l1_opy_ (u"ࠧࠨጩ"))
    def __1l11ll11ll1_opy_(self, event_name):
        if self.bstack11l11l1l1l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡲࡴࡵ࡯࡮ࡨࠢࡆࡐࡎࠨጪ"))
        self.__1l1l11l111l_opy_()
    def __1l1l1l1lll1_opy_(self, event_name, bstack1l1l111lll1_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack1l1_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠢጫ"))
        bstack1l11lll11ll_opy_ = Path(bstack1lll1llll11_opy_ (u"ࠣࡽࡶࡩࡱ࡬࠮ࡤ࡮࡬ࡣࡩ࡯ࡲࡾ࠱ࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࡶ࠲࡯ࡹ࡯࡯ࠤጬ"))
        if self.bstack1l1l1ll1l11_opy_ and bstack1l11lll11ll_opy_.exists():
            with open(bstack1l11lll11ll_opy_, bstack1l1_opy_ (u"ࠩࡵࠫጭ"), encoding=bstack1l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩጮ")) as fp:
                data = json.load(fp)
                try:
                    bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠫࡕࡕࡓࡕࠩጯ"), bstack11ll1ll1ll_opy_(bstack1l11lll111_opy_), data, {
                        bstack1l1_opy_ (u"ࠬࡧࡵࡵࡪࠪጰ"): (self.config[bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨጱ")], self.config[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪጲ")])
                    })
                except Exception as e:
                    logger.debug(bstack11ll11l1ll_opy_.format(str(e)))
            bstack1l11lll11ll_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l11l1ll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def __1l1l1ll11l1_opy_(self, event_name: str, data):
        from bstack_utils.bstack111l11l11_opy_ import bstack1lllllll11l_opy_
        self.bstack1l1l11l1lll_opy_, self.bstack1l1l1ll1l11_opy_ = bstack1l1l1lllll1_opy_(data.bs_config)
        os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡘࡔࡌࡘࡆࡈࡌࡆࡡࡇࡍࡗ࠭ጳ")] = self.bstack1l1l1ll1l11_opy_
        if not self.bstack1l1l11l1lll_opy_ or not self.bstack1l1l1ll1l11_opy_:
            raise ValueError(bstack1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸ࡭࡫ࠠࡔࡆࡎࠤࡈࡒࡉࠡࡤ࡬ࡲࡦࡸࡹࠣጴ"))
        if self.bstack11l11l1l1l_opy_():
            self.__1l11ll1l1l1_opy_(event_name, bstack11llll111l_opy_())
            return
        try:
            bstack1lllllll11l_opy_.end(EVENTS.bstack11ll11l11l_opy_.value, EVENTS.bstack11ll11l11l_opy_.value + bstack1l1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥጵ"), EVENTS.bstack11ll11l11l_opy_.value + bstack1l1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤጶ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1l1_opy_ (u"ࠧࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࠠࡔࡆࡎࠤࡘ࡫ࡴࡶࡲ࠱ࠦጷ"))
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡼࡿࠥጸ").format(e))
        start = datetime.now()
        is_started = self.__1l11ll1l1ll_opy_()
        self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠢࡴࡲࡤࡻࡳࡥࡴࡪ࡯ࡨࠦጹ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l11lll1l11_opy_()
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢጺ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1l11lll11_opy_(data)
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢጻ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l11lllll1l_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def __1l11ll1l1l1_opy_(self, event_name: str, data: bstack11llll111l_opy_):
        if not self.bstack11l11l1l1l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰࡰࡱࡩࡨࡺ࠺ࠡࡰࡲࡸࠥࡧࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢጼ"))
            return
        bin_session_id = os.environ.get(bstack1l11llll111_opy_)
        start = datetime.now()
        self.__1l11lll1l11_opy_()
        self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥጽ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1l1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠡࡶࡲࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡃࡍࡋࠣࠦጾ") + str(bin_session_id) + bstack1l1_opy_ (u"ࠨࠢጿ"))
        start = datetime.now()
        self.__1l11ll1ll11_opy_()
        self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧፀ"), datetime.now() - start)
    def __1l1l1111l11_opy_(self):
        if not self.bstack1llll1l11ll_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡥࡤࡲࡳࡵࡴࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࠤࡲࡵࡤࡶ࡮ࡨࡷࠧፁ"))
            return
        bstack1l1l1ll1l1l_opy_ = {
            bstack1l1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨፂ"): (bstack1ll1lll111l_opy_, bstack1lll1ll1l1l_opy_, bstack1llll111l11_opy_),
            bstack1l1_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧፃ"): (bstack1llll11lll1_opy_, bstack1lll11l1l11_opy_, bstack1llll1l11l1_opy_),
        }
        if not self.bstack1l1l1llll11_opy_ and self.session_framework in bstack1l1l1ll1l1l_opy_:
            bstack1l1l11ll111_opy_, bstack1l11ll1lll1_opy_, bstack1l1l1l1l1l1_opy_ = bstack1l1l1ll1l1l_opy_[self.session_framework]
            bstack1l1l11lllll_opy_ = bstack1l11ll1lll1_opy_()
            self.bstack1ll1ll1llll_opy_ = bstack1l1l11lllll_opy_
            self.bstack1l1l1llll11_opy_ = bstack1l1l1l1l1l1_opy_
            self.bstack1l1l111l111_opy_.append(bstack1l1l11lllll_opy_)
            self.bstack1l1l111l111_opy_.append(bstack1l1l11ll111_opy_(self.bstack1ll1ll1llll_opy_))
        if not self.bstack1l1ll111l1l_opy_ and self.config_observability and self.config_observability.success: # bstack1llll1ll111_opy_
            self.bstack1l1ll111l1l_opy_ = bstack1l11lll1111_opy_(self.bstack1l1l1llll11_opy_, self.bstack1ll1ll1llll_opy_) # bstack1l1l1ll111l_opy_
            self.bstack1l1l111l111_opy_.append(self.bstack1l1ll111l1l_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l1llll1l_opy_(self.bstack1l1l1llll11_opy_, self.bstack1ll1ll1llll_opy_)
            self.bstack1l1l111l111_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1l1_opy_ (u"ࠦࡸ࡫࡬ࡧࡊࡨࡥࡱࠨፄ"), False) == True:
            self.ai = bstack1l1ll1l111l_opy_()
            self.bstack1l1l111l111_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l1l11ll1_opy_ and self.bstack1l1l1l11ll1_opy_.success:
            self.percy = bstack1l1l111ll1l_opy_(self.bstack1l1l1l11ll1_opy_)
            self.bstack1l1l111l111_opy_.append(self.percy)
        for mod in self.bstack1l1l111l111_opy_:
            if not mod.bstack1lll11l1lll_opy_():
                mod.configure(self.bstack1llll1l11ll_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11l1ll1_opy_)
    def __1l1l11l11ll_opy_(self):
        for mod in self.bstack1l1l111l111_opy_:
            if mod.bstack1lll11l1lll_opy_():
                mod.configure(self.bstack1llll1l11ll_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l1l11111ll_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def __1l1l11lll11_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l11llllll1_opy_:
            return
        self.__1l11llll1l1_opy_(data)
        bstack1l1ll111l_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧፅ")
        req.sdk_language = bstack1l1_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨፆ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l11l1l11_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1l1_opy_ (u"ࠢ࡜ࠤፇ") + str(id(self)) + bstack1l1_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡷࡹࡧࡲࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢፈ"))
            r = self.bstack1llll1l11ll_opy_.StartBinSession(req)
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦፉ"), datetime.now() - bstack1l1ll111l_opy_)
            os.environ[bstack1l11llll111_opy_] = r.bin_session_id
            self.__1l11ll1llll_opy_(r)
            self.__1l1l1111l11_opy_()
            self.bstack1lll11l1ll1_opy_.start()
            self.bstack1l11llllll1_opy_ = True
            self.logger.debug(bstack1l1_opy_ (u"ࠥ࡟ࠧፊ") + str(id(self)) + bstack1l1_opy_ (u"ࠦࡢࠦ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠤፋ"))
        except grpc.bstack1l1l1lll111_opy_ as bstack1l1l1l11111_opy_:
            self.logger.error(bstack1l1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡹ࡯࡭ࡦࡱࡨࡹࡹ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢፌ") + str(bstack1l1l1l11111_opy_) + bstack1l1_opy_ (u"ࠨࠢፍ"))
            traceback.print_exc()
            raise bstack1l1l1l11111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦፎ") + str(e) + bstack1l1_opy_ (u"ࠣࠤፏ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l1ll11ll_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def __1l11ll1ll11_opy_(self):
        if not self.bstack11l11l1l1l_opy_() or not self.cli_bin_session_id or self.bstack1l11ll1ll1l_opy_:
            return
        bstack1l1ll111l_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩፐ"), bstack1l1_opy_ (u"ࠪ࠴ࠬፑ")))
        try:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡠࠨፒ") + str(id(self)) + bstack1l1_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢፓ"))
            r = self.bstack1llll1l11ll_opy_.ConnectBinSession(req)
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡨࡵ࡮࡯ࡧࡦࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥፔ"), datetime.now() - bstack1l1ll111l_opy_)
            self.__1l11ll1llll_opy_(r)
            self.__1l1l1111l11_opy_()
            self.bstack1lll11l1ll1_opy_.start()
            self.bstack1l11ll1ll1l_opy_ = True
            self.logger.debug(bstack1l1_opy_ (u"ࠢ࡜ࠤፕ") + str(id(self)) + bstack1l1_opy_ (u"ࠣ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠢፖ"))
        except grpc.bstack1l1l1lll111_opy_ as bstack1l1l1l11111_opy_:
            self.logger.error(bstack1l1_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦፗ") + str(bstack1l1l1l11111_opy_) + bstack1l1_opy_ (u"ࠥࠦፘ"))
            traceback.print_exc()
            raise bstack1l1l1l11111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣፙ") + str(e) + bstack1l1_opy_ (u"ࠧࠨፚ"))
            traceback.print_exc()
            raise e
    def __1l11ll1llll_opy_(self, r):
        self.bstack1l1ll1111l1_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1l1_opy_ (u"ࠨࡵ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡷࡪࡸࡶࡦࡴࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧ፛") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1l1_opy_ (u"ࠢࡦ࡯ࡳࡸࡾࠦࡣࡰࡰࡩ࡭࡬ࠦࡦࡰࡷࡱࡨࠧ፜"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡥࡳࡥࡼࠤ࡮ࡹࠠࡴࡧࡱࡸࠥࡵ࡮࡭ࡻࠣࡥࡸࠦࡰࡢࡴࡷࠤࡴ࡬ࠠࡵࡪࡨࠤࠧࡉ࡯࡯ࡰࡨࡧࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠮ࠥࠤࡦࡴࡤࠡࡶ࡫࡭ࡸࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡦࡲࡳࡰࠢࡸࡷࡪࡪࠠࡣࡻࠣࡗࡹࡧࡲࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪࡨࡶࡪ࡬࡯ࡳࡧ࠯ࠤࡓࡵ࡮ࡦࠢ࡫ࡥࡳࡪ࡬ࡪࡰࡪࠤ࡮ࡹࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ፝")
        self.bstack1l1l1l11ll1_opy_ = getattr(r, bstack1l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ፞"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ፟")] = self.config_testhub.jwt
        os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ፠")] = self.config_testhub.build_hashed_id
    def bstack1l1l11ll11l_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1ll111111_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1l111111l_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1l111111l_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1l11ll11l_opy_(event_name=EVENTS.bstack1l11ll1l111_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def __1l11ll1l1ll_opy_(self, bstack1l1ll111l11_opy_=10):
        if self.bstack1l1ll111111_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡹࡴࡢࡴࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠢ፡"))
            return True
        self.logger.debug(bstack1l1_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧ።"))
        if os.getenv(bstack1l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡉࡓ࡜ࠢ፣")) == bstack1l11llll11l_opy_:
            self.cli_bin_session_id = bstack1l11llll11l_opy_
            self.cli_listen_addr = bstack1l1_opy_ (u"ࠣࡷࡱ࡭ࡽࡀ࠯ࡵ࡯ࡳ࠳ࡸࡪ࡫࠮ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠰ࠩࡸ࠴ࡳࡰࡥ࡮ࠦ፤") % (self.cli_bin_session_id)
            self.bstack1l1ll111111_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l11l1lll_opy_, bstack1l1_opy_ (u"ࠤࡶࡨࡰࠨ፥")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1lll1ll_opy_ compat for text=True in bstack1l1l1lll11l_opy_ python
            encoding=bstack1l1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤ፦"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l11lll1lll_opy_ = threading.Thread(target=self.__1l1l111llll_opy_, args=(bstack1l1ll111l11_opy_,))
        bstack1l11lll1lll_opy_.start()
        bstack1l11lll1lll_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡷࡵࡧࡷ࡯࠼ࠣࡶࡪࡺࡵࡳࡰࡦࡳࡩ࡫࠽ࡼࡵࡨࡰ࡫࠴ࡰࡳࡱࡦࡩࡸࡹ࠮ࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࢁࠥࡵࡵࡵ࠿ࡾࡷࡪࡲࡦ࠯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡶࡸࡩࡵࡵࡵ࠰ࡵࡩࡦࡪࠨࠪࡿࠣࡩࡷࡸ࠽ࠣ፧") + str(self.process.stderr.read()) + bstack1l1_opy_ (u"ࠧࠨ፨"))
        if not self.bstack1l1ll111111_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠨ࡛ࠣ፩") + str(id(self)) + bstack1l1_opy_ (u"ࠢ࡞ࠢࡦࡰࡪࡧ࡮ࡶࡲࠥ፪"))
            self.__1l1l11l111l_opy_()
        self.logger.debug(bstack1l1_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡱࡴࡲࡧࡪࡹࡳࡠࡴࡨࡥࡩࡿ࠺ࠡࠤ፫") + str(self.bstack1l1ll111111_opy_) + bstack1l1_opy_ (u"ࠤࠥ፬"))
        return self.bstack1l1ll111111_opy_
    def __1l1l111llll_opy_(self, bstack1l1ll111ll1_opy_=10):
        bstack1l1l1l1ll1l_opy_ = time.time()
        while self.process and time.time() - bstack1l1l1l1ll1l_opy_ < bstack1l1ll111ll1_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1l1_opy_ (u"ࠥ࡭ࡩࡃࠢ፭") in line:
                    self.cli_bin_session_id = line.split(bstack1l1_opy_ (u"ࠦ࡮ࡪ࠽ࠣ፮"))[-1:][0].strip()
                    self.logger.debug(bstack1l1_opy_ (u"ࠧࡩ࡬ࡪࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦ࠽ࠦ፯") + str(self.cli_bin_session_id) + bstack1l1_opy_ (u"ࠨࠢ፰"))
                    continue
                if bstack1l1_opy_ (u"ࠢ࡭࡫ࡶࡸࡪࡴ࠽ࠣ፱") in line:
                    self.cli_listen_addr = line.split(bstack1l1_opy_ (u"ࠣ࡮࡬ࡷࡹ࡫࡮࠾ࠤ፲"))[-1:][0].strip()
                    self.logger.debug(bstack1l1_opy_ (u"ࠤࡦࡰ࡮ࡥ࡬ࡪࡵࡷࡩࡳࡥࡡࡥࡦࡵ࠾ࠧ፳") + str(self.cli_listen_addr) + bstack1l1_opy_ (u"ࠥࠦ፴"))
                    continue
                if bstack1l1_opy_ (u"ࠦࡵࡵࡲࡵ࠿ࠥ፵") in line:
                    port = line.split(bstack1l1_opy_ (u"ࠧࡶ࡯ࡳࡶࡀࠦ፶"))[-1:][0].strip()
                    self.logger.debug(bstack1l1_opy_ (u"ࠨࡰࡰࡴࡷ࠾ࠧ፷") + str(port) + bstack1l1_opy_ (u"ࠢࠣ፸"))
                    continue
                if line.strip() == bstack1l1l11l1l1l_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1l1_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡊࡑࡢࡗ࡙ࡘࡅࡂࡏࠥ፹"), bstack1l1_opy_ (u"ࠤ࠴ࠦ፺")) == bstack1l1_opy_ (u"ࠥ࠵ࠧ፻"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1ll111111_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1l1_opy_ (u"ࠦࡪࡸࡲࡰࡴ࠽ࠤࠧ፼") + str(e) + bstack1l1_opy_ (u"ࠧࠨ፽"))
        return False
    @measure(event_name=EVENTS.bstack1l11ll1l11l_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def __1l1l11l111l_opy_(self):
        if self.bstack1l1ll11111l_opy_:
            self.bstack1lll11l1ll1_opy_.stop()
            start = datetime.now()
            if self.bstack1l11lllllll_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l11ll1ll1l_opy_:
                    self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠨࡳࡵࡱࡳࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥ፾"), datetime.now() - start)
                else:
                    self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠢࡴࡶࡲࡴࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦ፿"), datetime.now() - start)
            self.__1l1l11l11ll_opy_()
            start = datetime.now()
            self.bstack1l1ll11111l_opy_.close()
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠣࡦ࡬ࡷࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥᎀ"), datetime.now() - start)
            self.bstack1l1ll11111l_opy_ = None
        if self.process:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡸࡴࡶࠢᎁ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠥ࡯࡮ࡲ࡬ࡠࡶ࡬ࡱࡪࠨᎂ"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l11l1111_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1l111lll1l_opy_()
                self.logger.info(
                    bstack1l1_opy_ (u"࡛ࠦ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠦᎃ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᎄ")] = self.config_testhub.build_hashed_id
        self.bstack1l1ll111111_opy_ = False
    def __1l11llll1l1_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1l1_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᎅ")] = selenium.__version__
            data.frameworks.append(bstack1l1_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᎆ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1l1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᎇ")] = __version__
            data.frameworks.append(bstack1l1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᎈ"))
        except:
            pass
    def bstack1l11ll11l1l_opy_(self, hub_url: str, platform_index: int, bstack111ll1llll_opy_: Any):
        if self.bstack1llll11ll1l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠤࡸ࡫ࡴࡶࡲࠣࡷࡪࡲࡥ࡯࡫ࡸࡱ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡴࡧࡷࠤࡺࡶࠢᎉ"))
            return
        try:
            bstack1l1ll111l_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1l1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᎊ")
            self.bstack1llll11ll1l_opy_ = bstack1llll1l11l1_opy_(
                cli.config.get(bstack1l1_opy_ (u"ࠧ࡮ࡵࡣࡗࡵࡰࠧᎋ"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1lllll11l1l_opy_={bstack1l1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥᎌ"): bstack111ll1llll_opy_}
            )
            def bstack1l1l1111ll1_opy_(self):
                return
            if self.config.get(bstack1l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠤᎍ"), True):
                Service.start = bstack1l1l1111ll1_opy_
                Service.stop = bstack1l1l1111ll1_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack1111lll1l_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11llllll_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᎎ"), datetime.now() - bstack1l1ll111l_opy_)
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡀࠠࠣᎏ") + str(e) + bstack1l1_opy_ (u"ࠥࠦ᎐"))
    def bstack1l11lll111l_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1ll1ll1ll1_opy_
            self.bstack1llll11ll1l_opy_ = bstack1llll111l11_opy_(
                platform_index,
                framework_name=bstack1l1_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ᎑"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠾ࠥࠨ᎒") + str(e) + bstack1l1_opy_ (u"ࠨࠢ᎓"))
            pass
    def bstack1l1l1l1l1ll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡶࡩࡹࠦࡵࡱࠤ᎔"))
            return
        if bstack1l11l11ll_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣ᎕"): pytest.__version__ }, [bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨ᎖")], self.bstack1lll11l1ll1_opy_, self.bstack1llll1l11ll_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l11ll11lll_opy_({ bstack1l1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ᎗"): pytest.__version__ }, [bstack1l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦ᎘")], self.bstack1lll11l1ll1_opy_, self.bstack1llll1l11ll_opy_)
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࠤ᎙") + str(e) + bstack1l1_opy_ (u"ࠨࠢ᎚"))
        self.bstack1l1l1ll1ll1_opy_()
    def bstack1l1l1ll1ll1_opy_(self):
        if not self.bstack1lllllll11_opy_():
            return
        bstack111ll11ll1_opy_ = None
        def bstack11ll1l1l11_opy_(config, startdir):
            return bstack1l1_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧ᎛").format(bstack1l1_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢ᎜"))
        def bstack1l11ll11ll_opy_():
            return
        def bstack11l1lll1l_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1l1_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩ᎝"):
                return bstack1l1_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ᎞")
            else:
                return bstack111ll11ll1_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack111ll11ll1_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack11ll1l1l11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l11ll11ll_opy_
            Config.getoption = bstack11l1lll1l_opy_
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡷࡧ࡭ࠦࡰࡺࡶࡨࡷࡹࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡨࡲࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠾ࠥࠨ᎟") + str(e) + bstack1l1_opy_ (u"ࠧࠨᎠ"))
    def bstack1l1l111l11l_opy_(self):
        bstack11111l1ll_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack11111l1ll_opy_, dict):
            if cli.config_observability:
                bstack11111l1ll_opy_.update(
                    {bstack1l1_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨᎡ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡡࡷࡳࡤࡽࡲࡢࡲࠥᎢ") in accessibility.get(bstack1l1_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᎣ"), {}):
                    bstack1l1l1l1l11l_opy_ = accessibility.get(bstack1l1_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᎤ"))
                    bstack1l1l1l1l11l_opy_.update({ bstack1l1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷ࡙ࡵࡗࡳࡣࡳࠦᎥ"): bstack1l1l1l1l11l_opy_.pop(bstack1l1_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢᎦ")) })
                bstack11111l1ll_opy_.update({bstack1l1_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧᎧ"): accessibility })
        return bstack11111l1ll_opy_
    @measure(event_name=EVENTS.bstack1l1l11llll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1l11lllllll_opy_(self, bstack1l1l1l1ll11_opy_: str = None, bstack1l1l1l111ll_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1llll1l11ll_opy_:
            return
        bstack1l1ll111l_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1l1ll11_opy_:
            req.bstack1l1l1l1ll11_opy_ = bstack1l1l1l1ll11_opy_
        if bstack1l1l1l111ll_opy_:
            req.bstack1l1l1l111ll_opy_ = bstack1l1l1l111ll_opy_
        try:
            r = self.bstack1llll1l11ll_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺ࡯ࡱࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᎨ"), datetime.now() - bstack1l1ll111l_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack111l1l11l1_opy_(self, key: str, value: timedelta):
        tag = bstack1l1_opy_ (u"ࠢࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢᎩ") if self.bstack11l11l1l1l_opy_() else bstack1l1_opy_ (u"ࠣ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹࠢᎪ")
        self.bstack1l1l1ll1111_opy_[bstack1l1_opy_ (u"ࠤ࠽ࠦᎫ").join([tag + bstack1l1_opy_ (u"ࠥ࠱ࠧᎬ") + str(id(self)), key])] += value
    def bstack1l111lll1l_opy_(self):
        if not os.getenv(bstack1l1_opy_ (u"ࠦࡉࡋࡂࡖࡉࡢࡔࡊࡘࡆࠣᎭ"), bstack1l1_opy_ (u"ࠧ࠶ࠢᎮ")) == bstack1l1_opy_ (u"ࠨ࠱ࠣᎯ"):
            return
        bstack1l11lllll11_opy_ = dict()
        bstack1lll1lllll1_opy_ = []
        if self.test_framework:
            bstack1lll1lllll1_opy_.extend(list(self.test_framework.bstack1lll1lllll1_opy_.values()))
        if self.bstack1llll11ll1l_opy_:
            bstack1lll1lllll1_opy_.extend(list(self.bstack1llll11ll1l_opy_.bstack1lll1lllll1_opy_.values()))
        for instance in bstack1lll1lllll1_opy_:
            if not instance.platform_index in bstack1l11lllll11_opy_:
                bstack1l11lllll11_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l11lllll11_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll11lll_opy_().items():
                report[k] += v
                report[k.split(bstack1l1_opy_ (u"ࠢ࠻ࠤᎰ"))[0]] += v
        bstack1l11lll1l1l_opy_ = sorted([(k, v) for k, v in self.bstack1l1l1ll1111_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l11lll1l_opy_ = 0
        for r in bstack1l11lll1l1l_opy_:
            bstack1l1l1111111_opy_ = r[1].total_seconds()
            bstack1l1l11lll1l_opy_ += bstack1l1l1111111_opy_
            self.logger.debug(bstack1l1_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࢁࡲ࡜࠲ࡠࢁࡂࠨᎱ") + str(bstack1l1l1111111_opy_) + bstack1l1_opy_ (u"ࠤࠥᎲ"))
        self.logger.debug(bstack1l1_opy_ (u"ࠥ࠱࠲ࠨᎳ"))
        bstack1l11lll11l1_opy_ = []
        for platform_index, report in bstack1l11lllll11_opy_.items():
            bstack1l11lll11l1_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l11lll11l1_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll11l11_opy_ = set()
        bstack1l1l1lll1l1_opy_ = 0
        for r in bstack1l11lll11l1_opy_:
            bstack1l1l1111111_opy_ = r[2].total_seconds()
            bstack1l1l1lll1l1_opy_ += bstack1l1l1111111_opy_
            bstack1lll11l11_opy_.add(r[0])
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡹ࡫ࡳࡵ࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࠱ࢀࡸ࡛࠱࡟ࢀ࠾ࢀࡸ࡛࠲࡟ࢀࡁࠧᎴ") + str(bstack1l1l1111111_opy_) + bstack1l1_opy_ (u"ࠧࠨᎵ"))
        if self.bstack11l11l1l1l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠨ࠭࠮ࠤᎶ"))
            self.logger.debug(bstack1l1_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࡁࢀࡺ࡯ࡵࡣ࡯ࡣࡨࡲࡩࡾࠢࡷࡩࡸࡺ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ࠰ࡿࡸࡺࡲࠩࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ࠭ࢂࡃࠢᎷ") + str(bstack1l1l1lll1l1_opy_) + bstack1l1_opy_ (u"ࠣࠤᎸ"))
        else:
            self.logger.debug(bstack1l1_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷࡂࠨᎹ") + str(bstack1l1l11lll1l_opy_) + bstack1l1_opy_ (u"ࠥࠦᎺ"))
        self.logger.debug(bstack1l1_opy_ (u"ࠦ࠲࠳ࠢᎻ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1llll1l11ll_opy_:
            self.logger.error(bstack1l1_opy_ (u"ࠧࡩ࡬ࡪࡡࡶࡩࡷࡼࡩࡤࡧࠣ࡭ࡸࠦ࡮ࡰࡶࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࡤ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤᎼ"))
            return None
        response = self.bstack1llll1l11ll_opy_.TestOrchestration(request)
        self.logger.debug(bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷ࠱ࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠱ࡸ࡫ࡳࡴ࡫ࡲࡲࡂࢁࡽࠣᎽ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1ll1111l1_opy_(self, r):
        if r is not None and getattr(r, bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࠨᎾ"), None) and getattr(r.testhub, bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨᎿ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1l1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᏀ")))
            for bstack1l1l1111lll_opy_, err in errors.items():
                if err[bstack1l1_opy_ (u"ࠪࡸࡾࡶࡥࠨᏁ")] == bstack1l1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᏂ"):
                    self.logger.info(err[bstack1l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ꮓ")])
                else:
                    self.logger.error(err[bstack1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᏄ")])
    def bstack111lll1l1l_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()