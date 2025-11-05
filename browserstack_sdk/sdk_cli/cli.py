# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import bstack1l11ll1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll111l1l_opy_ import bstack1l1ll11ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1ll1l1l_opy_ import bstack1l1l1l1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1lllll1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll1ll11_opy_ import bstack1ll1lll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1l1_opy_ import bstack1lll1ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1l11111ll_opy_ import bstack1l1l1llll11_opy_
from browserstack_sdk.sdk_cli.bstack11l1l1l1l_opy_ import bstack11l1l1l1l_opy_, Events, bstack111ll1l11_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1lll11l_opy_ import bstack1l11lll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import bstack1lll111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1lll111_opy_
from bstack_utils.helper import Notset, bstack1l11llll1l1_opy_, get_cli_dir, bstack1l1l1111ll1_opy_, bstack11llll111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll11111ll1_opy_ import bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1111l1_opy_ import bstack1l11111111_opy_
from bstack_utils.helper import Notset, bstack1l11llll1l1_opy_, get_cli_dir, bstack1l1l1111ll1_opy_, bstack11llll111l_opy_, bstack1l11l1111_opy_, bstack1ll1l1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll111111_opy_, bstack1lll11lll11_opy_, bstack1l1lllll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import bstack1lllllll11l_opy_, bstack1111111111_opy_, bstack1llll1lllll_opy_
from bstack_utils.constants import *
from bstack_utils.bstack11l11ll111_opy_ import bstack11111lll11_opy_
from bstack_utils import bstack11ll1111l_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l1111ll1_opy_, bstack1111lll1l_opy_
logger = bstack11ll1111l_opy_.get_logger(__name__, bstack11ll1111l_opy_.bstack1l11ll111l1_opy_())
def bstack1l1l1l11ll1_opy_(bs_config):
    bstack1l11lll11l1_opy_ = None
    bstack1l1l1l1lll1_opy_ = None
    try:
        bstack1l1l1l1lll1_opy_ = get_cli_dir()
        bstack1l11lll11l1_opy_ = bstack1l1l1111ll1_opy_(bstack1l1l1l1lll1_opy_)
        bstack1l1ll11111l_opy_ = bstack1l11llll1l1_opy_(bstack1l11lll11l1_opy_, bstack1l1l1l1lll1_opy_, bs_config)
        bstack1l11lll11l1_opy_ = bstack1l1ll11111l_opy_ if bstack1l1ll11111l_opy_ else bstack1l11lll11l1_opy_
        if not bstack1l11lll11l1_opy_:
            raise ValueError(bstack1lll11l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠧጂ"))
    except Exception as ex:
        logger.debug(bstack1lll11l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡺࡨࡦࠢ࡯ࡥࡹ࡫ࡳࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡾࢁࠧጃ").format(ex))
        bstack1l11lll11l1_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠨጄ"))
        if bstack1l11lll11l1_opy_:
            logger.debug(bstack1lll11l_opy_ (u"ࠦࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠢࡩࡶࡴࡳࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸ࠿ࠦࠢጅ") + str(bstack1l11lll11l1_opy_) + bstack1lll11l_opy_ (u"ࠧࠨጆ"))
        else:
            logger.debug(bstack1lll11l_opy_ (u"ࠨࡎࡰࠢࡹࡥࡱ࡯ࡤࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷ࠿ࠥࡹࡥࡵࡷࡳࠤࡲࡧࡹࠡࡤࡨࠤ࡮ࡴࡣࡰ࡯ࡳࡰࡪࡺࡥ࠯ࠤጇ"))
    return bstack1l11lll11l1_opy_, bstack1l1l1l1lll1_opy_
bstack1l1l1ll11l1_opy_ = bstack1lll11l_opy_ (u"ࠢ࠺࠻࠼࠽ࠧገ")
bstack1l1l1llllll_opy_ = bstack1lll11l_opy_ (u"ࠣࡴࡨࡥࡩࡿࠢጉ")
bstack1l11lllll1l_opy_ = bstack1lll11l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡖࡉࡘ࡙ࡉࡐࡐࡢࡍࡉࠨጊ")
bstack1l11ll11ll1_opy_ = bstack1lll11l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡐࡎ࡙ࡔࡆࡐࡢࡅࡉࡊࡒࠣጋ")
bstack111ll1llll_opy_ = bstack1lll11l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠢጌ")
bstack1l1l11lll11_opy_ = re.compile(bstack1lll11l_opy_ (u"ࡷࠨࠨࡀ࡫ࠬ࠲࠯࠮ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࢁࡈࡓࠪ࠰࠭ࠦግ"))
bstack1l1l1l1ll1l_opy_ = bstack1lll11l_opy_ (u"ࠨࡤࡦࡸࡨࡰࡴࡶ࡭ࡦࡰࡷࠦጎ")
bstack1l11lllllll_opy_ = bstack1lll11l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡐࡔࡆࡉࡤࡌࡁࡍࡎࡅࡅࡈࡑࠢጏ")
bstack1l1l1l11l1l_opy_ = [
    Events.bstack11l11ll1l1_opy_,
    Events.CONNECT,
    Events.bstack1l11l11l1l_opy_,
]
class SDKCLI:
    _1ll1l1lll11_opy_ = None
    process: Union[None, Any]
    bstack1l11llllll1_opy_: bool
    bstack1l1l11l1l11_opy_: bool
    bstack1l1l1ll111l_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l11ll1lll1_opy_: Union[None, grpc.Channel]
    bstack1l1l1l1111l_opy_: str
    test_framework: TestFramework
    bstack1lllll11lll_opy_: bstack1lll111lll1_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l1l111l1_opy_: bstack1l1l1llll11_opy_
    accessibility: bstack1l11ll1ll1l_opy_
    bstack111l1111l1_opy_: bstack1l11111111_opy_
    ai: bstack1l1ll11ll1l_opy_
    bstack1l1l11ll111_opy_: bstack1l1l1l1l1ll_opy_
    bstack1l1l1ll11ll_opy_: List[bstack1lllllll1l1_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l11l11l1_opy_: Any
    bstack1l1l1lll1ll_opy_: Dict[str, timedelta]
    bstack1l1l1l1ll11_opy_: str
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_
    def __new__(cls):
        if not cls._1ll1l1lll11_opy_:
            cls._1ll1l1lll11_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1l1lll11_opy_
    def __init__(self):
        self.process = None
        self.bstack1l11llllll1_opy_ = False
        self.bstack1l11ll1lll1_opy_ = None
        self.bstack1llll11l11l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l11ll11ll1_opy_, None)
        self.bstack1l1l11l11ll_opy_ = os.environ.get(bstack1l11lllll1l_opy_, bstack1lll11l_opy_ (u"ࠣࠤጐ")) == bstack1lll11l_opy_ (u"ࠤࠥ጑")
        self.bstack1l1l11l1l11_opy_ = False
        self.bstack1l1l1ll111l_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l11l11l1_opy_ = None
        self.test_framework = None
        self.bstack1lllll11lll_opy_ = None
        self.bstack1l1l1l1111l_opy_=bstack1lll11l_opy_ (u"ࠥࠦጒ")
        self.session_framework = None
        self.logger = bstack11ll1111l_opy_.get_logger(self.__class__.__name__, bstack11ll1111l_opy_.bstack1l11ll111l1_opy_())
        self.bstack1l1l1lll1ll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11l1l1l_opy_ = bstack1lll11l1l11_opy_()
        self.bstack1l1l1l11l11_opy_ = None
        self.bstack1ll1lll111l_opy_ = None
        self.bstack1l1l1l111l1_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l1ll11ll_opy_ = []
    def bstack11111lll1l_opy_(self):
        return os.environ.get(bstack111ll1llll_opy_).lower().__eq__(bstack1lll11l_opy_ (u"ࠦࡹࡸࡵࡦࠤጓ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l11lllllll_opy_, bstack1lll11l_opy_ (u"ࠬ࠭ጔ")).lower() in [bstack1lll11l_opy_ (u"࠭ࡴࡳࡷࡨࠫጕ"), bstack1lll11l_opy_ (u"ࠧ࠲ࠩ጖"), bstack1lll11l_opy_ (u"ࠨࡻࡨࡷࠬ጗")]:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡉࡳࡷࡩࡩ࡯ࡩࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡳ࡯ࡥࡧࠣࡨࡺ࡫ࠠࡵࡱࠣࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡓࡗࡉࡅࡠࡈࡄࡐࡑࡈࡁࡄࡍࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴࠡࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠥጘ"))
            os.environ[bstack1lll11l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨጙ")] = bstack1lll11l_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥጚ")
            return False
        if bstack1lll11l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩጛ") in config and str(config[bstack1lll11l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪጜ")]).lower() != bstack1lll11l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ጝ"):
            return False
        bstack1l1l111111l_opy_ = [bstack1lll11l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣጞ"), bstack1lll11l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨጟ")]
        bstack1l11llll11l_opy_ = config.get(bstack1lll11l_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨጠ")) in bstack1l1l111111l_opy_ or os.environ.get(bstack1lll11l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬጡ")) in bstack1l1l111111l_opy_
        os.environ[bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣጢ")] = str(bstack1l11llll11l_opy_) # bstack1l1l1ll1ll1_opy_ bstack1l1l11l1ll1_opy_ VAR to bstack1l1l1lllll1_opy_ is binary running
        return bstack1l11llll11l_opy_
    def bstack1l11lll1l_opy_(self):
        for event in bstack1l1l1l11l1l_opy_:
            bstack11l1l1l1l_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack11l1l1l1l_opy_.logger.debug(bstack1lll11l_opy_ (u"ࠨࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠥࡃ࠾ࠡࡽࡤࡶ࡬ࡹࡽࠡࠤጣ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠢࠣጤ"))
            )
        bstack11l1l1l1l_opy_.register(Events.bstack11l11ll1l1_opy_, self.__1l11ll11l1l_opy_)
        bstack11l1l1l1l_opy_.register(Events.CONNECT, self.__1l1l111lll1_opy_)
        bstack11l1l1l1l_opy_.register(Events.bstack1l11l11l1l_opy_, self.__1l1l1111111_opy_)
        bstack11l1l1l1l_opy_.register(Events.bstack111l11ll1l_opy_, self.__1l11lll1ll1_opy_)
    def bstack1l1111lll_opy_(self):
        return not self.bstack1l1l11l11ll_opy_ and os.environ.get(bstack1l11lllll1l_opy_, bstack1lll11l_opy_ (u"ࠣࠤጥ")) != bstack1lll11l_opy_ (u"ࠤࠥጦ")
    def is_running(self):
        if self.bstack1l1l11l11ll_opy_:
            return self.bstack1l11llllll1_opy_
        else:
            return bool(self.bstack1l11ll1lll1_opy_)
    def bstack1l11lllll11_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l1ll11ll_opy_) and cli.is_running()
    def __1l11lll111l_opy_(self, bstack1l11llll1ll_opy_=10):
        if self.bstack1llll11l11l_opy_:
            return
        bstack11ll11l1l_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l11ll11ll1_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠥ࡟ࠧጧ") + str(id(self)) + bstack1lll11l_opy_ (u"ࠦࡢࠦࡣࡰࡰࡱࡩࡨࡺࡩ࡯ࡩࠥጨ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1lll11l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠱ࡩࡳࡧࡢ࡭ࡧࡢ࡬ࡹࡺࡰࡠࡲࡵࡳࡽࡿࠢጩ"), 0), (bstack1lll11l_opy_ (u"ࠨࡧࡳࡲࡦ࠲ࡪࡴࡡࡣ࡮ࡨࡣ࡭ࡺࡴࡱࡵࡢࡴࡷࡵࡸࡺࠤጪ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l11llll1ll_opy_)
        self.bstack1l11ll1lll1_opy_ = channel
        self.bstack1llll11l11l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l11ll1lll1_opy_)
        self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡩ࡯࡯ࡰࡨࡧࡹࠨጫ"), datetime.now() - bstack11ll11l1l_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l11ll11ll1_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1lll11l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦ࠽ࠤ࡮ࡹ࡟ࡤࡪ࡬ࡰࡩࡥࡰࡳࡱࡦࡩࡸࡹ࠽ࠣጬ") + str(self.bstack1l1111lll_opy_()) + bstack1lll11l_opy_ (u"ࠤࠥጭ"))
    def __1l1l1111111_opy_(self, event_name):
        if self.bstack1l1111lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡸࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡃࡍࡋࠥጮ"))
        self.__1l1l11111l1_opy_()
    def __1l11lll1ll1_opy_(self, event_name, bstack1l1ll1111l1_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack1lll11l_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠦጯ"))
        bstack1l1l11llll1_opy_ = Path(bstack1lll1ll1l11_opy_ (u"ࠧࢁࡳࡦ࡮ࡩ࠲ࡨࡲࡩࡠࡦ࡬ࡶࢂ࠵ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࡳ࠯࡬ࡶࡳࡳࠨጰ"))
        if self.bstack1l1l1l1lll1_opy_ and bstack1l1l11llll1_opy_.exists():
            with open(bstack1l1l11llll1_opy_, bstack1lll11l_opy_ (u"࠭ࡲࠨጱ"), encoding=bstack1lll11l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ጲ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠨࡒࡒࡗ࡙࠭ጳ"), bstack11111lll11_opy_(bstack1l1111111l_opy_), data, {
                        bstack1lll11l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧጴ"): (self.config[bstack1lll11l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬጵ")], self.config[bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧጶ")])
                    })
                except Exception as e:
                    logger.debug(bstack1111lll1l_opy_.format(str(e)))
            bstack1l1l11llll1_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l11ll11l11_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1l11ll11l1l_opy_(self, event_name: str, data):
        from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
        self.bstack1l1l1l1111l_opy_, self.bstack1l1l1l1lll1_opy_ = bstack1l1l1l11ll1_opy_(data.bs_config)
        os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡜ࡘࡉࡕࡃࡅࡐࡊࡥࡄࡊࡔࠪጷ")] = self.bstack1l1l1l1lll1_opy_
        if not self.bstack1l1l1l1111l_opy_ or not self.bstack1l1l1l1lll1_opy_:
            raise ValueError(bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡵࡪࡨࠤࡘࡊࡋࠡࡅࡏࡍࠥࡨࡩ࡯ࡣࡵࡽࠧጸ"))
        if self.bstack1l1111lll_opy_():
            self.__1l1l111lll1_opy_(event_name, bstack111ll1l11_opy_())
            return
        try:
            bstack1llll1l1l1l_opy_.end(EVENTS.bstack11l1llll11_opy_.value, EVENTS.bstack11l1llll11_opy_.value + bstack1lll11l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢጹ"), EVENTS.bstack11l1llll11_opy_.value + bstack1lll11l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨጺ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1lll11l_opy_ (u"ࠤࡆࡳࡲࡶ࡬ࡦࡶࡨࠤࡘࡊࡋࠡࡕࡨࡸࡺࡶ࠮ࠣጻ"))
        except Exception as e:
            logger.debug(bstack1lll11l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࢀࢃࠢጼ").format(e))
        start = datetime.now()
        is_started = self.__1l1l1111lll_opy_()
        self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦࡸࡶࡡࡸࡰࡢࡸ࡮ࡳࡥࠣጽ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l11lll111l_opy_()
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࡥࡴࡪ࡯ࡨࠦጾ"), datetime.now() - start)
            start = datetime.now()
            self.__1l11llll111_opy_(data)
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦጿ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l111llll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1l1l111lll1_opy_(self, event_name: str, data: bstack111ll1l11_opy_):
        if not self.bstack1l1111lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡴ࡮ࡦࡥࡷ࠾ࠥࡴ࡯ࡵࠢࡤࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦፀ"))
            return
        bin_session_id = os.environ.get(bstack1l11lllll1l_opy_)
        start = datetime.now()
        self.__1l11lll111l_opy_()
        self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢፁ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1lll11l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠥࡺ࡯ࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡇࡑࡏࠠࠣፂ") + str(bin_session_id) + bstack1lll11l_opy_ (u"ࠥࠦፃ"))
        start = datetime.now()
        self.__1l1l111l1ll_opy_()
        self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤፄ"), datetime.now() - start)
    def __1l11ll1l1ll_opy_(self):
        if not self.bstack1llll11l11l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࠡ࡯ࡲࡨࡺࡲࡥࡴࠤፅ"))
            return
        bstack1l1l1l111ll_opy_ = {
            bstack1lll11l_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥፆ"): (bstack1ll1lll11l1_opy_, bstack1lll1ll11l1_opy_, bstack1lll1lll111_opy_),
            bstack1lll11l_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤፇ"): (bstack1lllll1l1ll_opy_, bstack1lll11l1111_opy_, bstack1llllll1ll1_opy_),
        }
        if not self.bstack1l1l1l11l11_opy_ and self.session_framework in bstack1l1l1l111ll_opy_:
            bstack1l1l11l111l_opy_, bstack1l1ll1111ll_opy_, bstack1l11ll1ll11_opy_ = bstack1l1l1l111ll_opy_[self.session_framework]
            bstack1l11lll1l11_opy_ = bstack1l1ll1111ll_opy_()
            self.bstack1ll1lll111l_opy_ = bstack1l11lll1l11_opy_
            self.bstack1l1l1l11l11_opy_ = bstack1l11ll1ll11_opy_
            self.bstack1l1l1ll11ll_opy_.append(bstack1l11lll1l11_opy_)
            self.bstack1l1l1ll11ll_opy_.append(bstack1l1l11l111l_opy_(self.bstack1ll1lll111l_opy_))
        if not self.bstack1l1l1l111l1_opy_ and self.config_observability and self.config_observability.success: # bstack1lllll11ll1_opy_
            self.bstack1l1l1l111l1_opy_ = bstack1l1l1llll11_opy_(self.bstack1l1l1l11l11_opy_, self.bstack1ll1lll111l_opy_) # bstack1l1l1111l11_opy_
            self.bstack1l1l1ll11ll_opy_.append(self.bstack1l1l1l111l1_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l11ll1ll1l_opy_(self.bstack1l1l1l11l11_opy_, self.bstack1ll1lll111l_opy_)
            self.bstack1l1l1ll11ll_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1lll11l_opy_ (u"ࠣࡵࡨࡰ࡫ࡎࡥࡢ࡮ࠥፈ"), False) == True:
            self.ai = bstack1l1ll11ll1l_opy_()
            self.bstack1l1l1ll11ll_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l11l11l1_opy_ and self.bstack1l1l11l11l1_opy_.success:
            self.percy = bstack1l1l1l1l1ll_opy_(self.bstack1l1l11l11l1_opy_)
            self.bstack1l1l1ll11ll_opy_.append(self.percy)
        for mod in self.bstack1l1l1ll11ll_opy_:
            if not mod.bstack1lll11l11ll_opy_():
                mod.configure(self.bstack1llll11l11l_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11l1l1l_opy_)
    def __1l1l11l1111_opy_(self):
        for mod in self.bstack1l1l1ll11ll_opy_:
            if mod.bstack1lll11l11ll_opy_():
                mod.configure(self.bstack1llll11l11l_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l11ll1l111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1l11llll111_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l11l1l11_opy_:
            return
        self.__1l1l11ll1l1_opy_(data)
        bstack11ll11l1l_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1lll11l_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤፉ")
        req.sdk_language = bstack1lll11l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥፊ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l11lll11_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡠࠨፋ") + str(id(self)) + bstack1lll11l_opy_ (u"ࠧࡣࠠ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦፌ"))
            r = self.bstack1llll11l11l_opy_.StartBinSession(req)
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺࡡࡳࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣፍ"), datetime.now() - bstack11ll11l1l_opy_)
            os.environ[bstack1l11lllll1l_opy_] = r.bin_session_id
            self.__1l11ll1llll_opy_(r)
            self.__1l11ll1l1ll_opy_()
            self.bstack1lll11l1l1l_opy_.start()
            self.bstack1l1l11l1l11_opy_ = True
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢ࡜ࠤፎ") + str(id(self)) + bstack1lll11l_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠨፏ"))
        except grpc.bstack1l1l11lll1l_opy_ as bstack1l1l1l1l1l1_opy_:
            self.logger.error(bstack1lll11l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦፐ") + str(bstack1l1l1l1l1l1_opy_) + bstack1lll11l_opy_ (u"ࠥࠦፑ"))
            traceback.print_exc()
            raise bstack1l1l1l1l1l1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣፒ") + str(e) + bstack1lll11l_opy_ (u"ࠧࠨፓ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l1ll1111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1l1l111l1ll_opy_(self):
        if not self.bstack1l1111lll_opy_() or not self.cli_bin_session_id or self.bstack1l1l1ll111l_opy_:
            return
        bstack11ll11l1l_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ፔ"), bstack1lll11l_opy_ (u"ࠧ࠱ࠩፕ")))
        try:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣ࡝ࠥፖ") + str(id(self)) + bstack1lll11l_opy_ (u"ࠤࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦፗ"))
            r = self.bstack1llll11l11l_opy_.ConnectBinSession(req)
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢፘ"), datetime.now() - bstack11ll11l1l_opy_)
            self.__1l11ll1llll_opy_(r)
            self.__1l11ll1l1ll_opy_()
            self.bstack1lll11l1l1l_opy_.start()
            self.bstack1l1l1ll111l_opy_ = True
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡠࠨፙ") + str(id(self)) + bstack1lll11l_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠦፚ"))
        except grpc.bstack1l1l11lll1l_opy_ as bstack1l1l1l1l1l1_opy_:
            self.logger.error(bstack1lll11l_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡺࡩ࡮ࡧࡲࡩࡺࡺ࠭ࡦࡴࡵࡳࡷࡀࠠࠣ፛") + str(bstack1l1l1l1l1l1_opy_) + bstack1lll11l_opy_ (u"ࠢࠣ፜"))
            traceback.print_exc()
            raise bstack1l1l1l1l1l1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ፝") + str(e) + bstack1lll11l_opy_ (u"ࠤࠥ፞"))
            traceback.print_exc()
            raise e
    def __1l11ll1llll_opy_(self, r):
        self.bstack1l1l1l1llll_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1lll11l_opy_ (u"ࠥࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡴࡧࡵࡺࡪࡸࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤ፟") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1lll11l_opy_ (u"ࠦࡪࡳࡰࡵࡻࠣࡧࡴࡴࡦࡪࡩࠣࡪࡴࡻ࡮ࡥࠤ፠"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1lll11l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡩࡷࡩࡹࠡ࡫ࡶࠤࡸ࡫࡮ࡵࠢࡲࡲࡱࡿࠠࡢࡵࠣࡴࡦࡸࡴࠡࡱࡩࠤࡹ࡮ࡥࠡࠤࡆࡳࡳࡴࡥࡤࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠲ࠢࠡࡣࡱࡨࠥࡺࡨࡪࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡣ࡯ࡷࡴࠦࡵࡴࡧࡧࠤࡧࡿࠠࡔࡶࡤࡶࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࡳࡧࡩࡳࡷ࡫ࠬࠡࡐࡲࡲࡪࠦࡨࡢࡰࡧࡰ࡮ࡴࡧࠡ࡫ࡶࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ፡")
        self.bstack1l1l11l11l1_opy_ = getattr(r, bstack1lll11l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ።"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ፣")] = self.config_testhub.jwt
        os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭፤")] = self.config_testhub.build_hashed_id
    def bstack1l1l1ll1lll_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l11llllll1_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l11ll1l11l_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l11ll1l11l_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1l1ll1lll_opy_(event_name=EVENTS.bstack1l1l11lllll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1l1l1111lll_opy_(self, bstack1l11llll1ll_opy_=10):
        if self.bstack1l11llllll1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡶࡸࡦࡸࡴ࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡶࡺࡴ࡮ࡪࡰࡪࠦ፥"))
            return True
        self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡷࡹࡧࡲࡵࠤ፦"))
        if os.getenv(bstack1lll11l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡆࡐ࡙ࠦ፧")) == bstack1l1l1l1ll1l_opy_:
            self.cli_bin_session_id = bstack1l1l1l1ll1l_opy_
            self.cli_listen_addr = bstack1lll11l_opy_ (u"ࠧࡻ࡮ࡪࡺ࠽࠳ࡹࡳࡰ࠰ࡵࡧ࡯࠲ࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࠦࡵ࠱ࡷࡴࡩ࡫ࠣ፨") % (self.cli_bin_session_id)
            self.bstack1l11llllll1_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l1l1111l_opy_, bstack1lll11l_opy_ (u"ࠨࡳࡥ࡭ࠥ፩")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1111l1l_opy_ compat for text=True in bstack1l1l1l1l11l_opy_ python
            encoding=bstack1lll11l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨ፪"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1l111ll1l_opy_ = threading.Thread(target=self.__1l1l1l11111_opy_, args=(bstack1l11llll1ll_opy_,))
        bstack1l1l111ll1l_opy_.start()
        bstack1l1l111ll1l_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡴࡲࡤࡻࡳࡀࠠࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࡁࢀࡹࡥ࡭ࡨ࠱ࡴࡷࡵࡣࡦࡵࡶ࠲ࡷ࡫ࡴࡶࡴࡱࡧࡴࡪࡥࡾࠢࡲࡹࡹࡃࡻࡴࡧ࡯ࡪ࠳ࡶࡲࡰࡥࡨࡷࡸ࠴ࡳࡵࡦࡲࡹࡹ࠴ࡲࡦࡣࡧࠬ࠮ࢃࠠࡦࡴࡵࡁࠧ፫") + str(self.process.stderr.read()) + bstack1lll11l_opy_ (u"ࠤࠥ፬"))
        if not self.bstack1l11llllll1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥ࡟ࠧ፭") + str(id(self)) + bstack1lll11l_opy_ (u"ࠦࡢࠦࡣ࡭ࡧࡤࡲࡺࡶࠢ፮"))
            self.__1l1l11111l1_opy_()
        self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡵࡸ࡯ࡤࡧࡶࡷࡤࡸࡥࡢࡦࡼ࠾ࠥࠨ፯") + str(self.bstack1l11llllll1_opy_) + bstack1lll11l_opy_ (u"ࠨࠢ፰"))
        return self.bstack1l11llllll1_opy_
    def __1l1l1l11111_opy_(self, bstack1l1l1lll1l1_opy_=10):
        bstack1l11lll11ll_opy_ = time.time()
        while self.process and time.time() - bstack1l11lll11ll_opy_ < bstack1l1l1lll1l1_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1lll11l_opy_ (u"ࠢࡪࡦࡀࠦ፱") in line:
                    self.cli_bin_session_id = line.split(bstack1lll11l_opy_ (u"ࠣ࡫ࡧࡁࠧ፲"))[-1:][0].strip()
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡦࡰ࡮ࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠺ࠣ፳") + str(self.cli_bin_session_id) + bstack1lll11l_opy_ (u"ࠥࠦ፴"))
                    continue
                if bstack1lll11l_opy_ (u"ࠦࡱ࡯ࡳࡵࡧࡱࡁࠧ፵") in line:
                    self.cli_listen_addr = line.split(bstack1lll11l_opy_ (u"ࠧࡲࡩࡴࡶࡨࡲࡂࠨ፶"))[-1:][0].strip()
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡣ࡭࡫ࡢࡰ࡮ࡹࡴࡦࡰࡢࡥࡩࡪࡲ࠻ࠤ፷") + str(self.cli_listen_addr) + bstack1lll11l_opy_ (u"ࠢࠣ፸"))
                    continue
                if bstack1lll11l_opy_ (u"ࠣࡲࡲࡶࡹࡃࠢ፹") in line:
                    port = line.split(bstack1lll11l_opy_ (u"ࠤࡳࡳࡷࡺ࠽ࠣ፺"))[-1:][0].strip()
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡴࡴࡸࡴ࠻ࠤ፻") + str(port) + bstack1lll11l_opy_ (u"ࠦࠧ፼"))
                    continue
                if line.strip() == bstack1l1l1llllll_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1lll11l_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡎࡕ࡟ࡔࡖࡕࡉࡆࡓࠢ፽"), bstack1lll11l_opy_ (u"ࠨ࠱ࠣ፾")) == bstack1lll11l_opy_ (u"ࠢ࠲ࠤ፿"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l11llllll1_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡧࡵࡶࡴࡸ࠺ࠡࠤᎀ") + str(e) + bstack1lll11l_opy_ (u"ࠤࠥᎁ"))
        return False
    @measure(event_name=EVENTS.bstack1l1l111l11l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1l1l11111l1_opy_(self):
        if self.bstack1l11ll1lll1_opy_:
            self.bstack1lll11l1l1l_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l11ll1ll_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l1ll111l_opy_:
                    self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠥࡷࡹࡵࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢᎂ"), datetime.now() - start)
                else:
                    self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦࡸࡺ࡯ࡱࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣᎃ"), datetime.now() - start)
            self.__1l1l11l1111_opy_()
            start = datetime.now()
            self.bstack1l11ll1lll1_opy_.close()
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠧࡪࡩࡴࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢᎄ"), datetime.now() - start)
            self.bstack1l11ll1lll1_opy_ = None
        if self.process:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡳࡵࡱࡳࠦᎅ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠢ࡬࡫࡯ࡰࡤࡺࡩ࡮ࡧࠥᎆ"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l11l11ll_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1111l1111_opy_()
                self.logger.info(
                    bstack1lll11l_opy_ (u"ࠣࡘ࡬ࡷ࡮ࡺࠠࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠣᎇ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᎈ")] = self.config_testhub.build_hashed_id
        self.bstack1l11llllll1_opy_ = False
    def __1l1l11ll1l1_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1lll11l_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᎉ")] = selenium.__version__
            data.frameworks.append(bstack1lll11l_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᎊ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1lll11l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᎋ")] = __version__
            data.frameworks.append(bstack1lll11l_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᎌ"))
        except:
            pass
    def bstack1l1l1lll111_opy_(self, hub_url: str, platform_index: int, bstack1ll1l111ll_opy_: Any):
        if self.bstack1lllll11lll_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡸ࡫ࡴࠡࡷࡳࠦᎍ"))
            return
        try:
            bstack11ll11l1l_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1lll11l_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥᎎ")
            self.bstack1lllll11lll_opy_ = bstack1llllll1ll1_opy_(
                cli.config.get(bstack1lll11l_opy_ (u"ࠤ࡫ࡹࡧ࡛ࡲ࡭ࠤᎏ"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll1l1l11_opy_={bstack1lll11l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡢࡳࡵࡺࡩࡰࡰࡶࡣ࡫ࡸ࡯࡮ࡡࡦࡥࡵࡹࠢ᎐"): bstack1ll1l111ll_opy_}
            )
            def bstack1l11lll1111_opy_(self):
                return
            if self.config.get(bstack1lll11l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠨ᎑"), True):
                Service.start = bstack1l11lll1111_opy_
                Service.stop = bstack1l11lll1111_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack1l11111111_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll1l1l1ll1_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ᎒"), datetime.now() - bstack11ll11l1l_opy_)
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡵࡨࡰࡪࡴࡩࡶ࡯࠽ࠤࠧ᎓") + str(e) + bstack1lll11l_opy_ (u"ࠢࠣ᎔"))
    def bstack1l11lll1l1l_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack11ll1111l1_opy_
            self.bstack1lllll11lll_opy_ = bstack1lll1lll111_opy_(
                platform_index,
                framework_name=bstack1lll11l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ᎕"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠻ࠢࠥ᎖") + str(e) + bstack1lll11l_opy_ (u"ࠥࠦ᎗"))
            pass
    def bstack1l1l1ll1l11_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡳࡦࡶࠣࡹࡵࠨ᎘"))
            return
        if bstack11llll111l_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1lll11l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ᎙"): pytest.__version__ }, [bstack1lll11l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥ᎚")], self.bstack1lll11l1l1l_opy_, self.bstack1llll11l11l_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l11lll1lll_opy_({ bstack1lll11l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢ᎛"): pytest.__version__ }, [bstack1lll11l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣ᎜")], self.bstack1lll11l1l1l_opy_, self.bstack1llll11l11l_opy_)
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࠨ᎝") + str(e) + bstack1lll11l_opy_ (u"ࠥࠦ᎞"))
        self.bstack1l1l1l1l111_opy_()
    def bstack1l1l1l1l111_opy_(self):
        if not self.bstack11111lll1l_opy_():
            return
        bstack1ll111l11_opy_ = None
        def bstack1ll1111l1l_opy_(config, startdir):
            return bstack1lll11l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤ᎟").format(bstack1lll11l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦᎠ"))
        def bstack1l111111ll_opy_():
            return
        def bstack1l11111l11_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1lll11l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭Ꭱ"):
                return bstack1lll11l_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨᎢ")
            else:
                return bstack1ll111l11_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1ll111l11_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1ll1111l1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l111111ll_opy_
            Config.getoption = bstack1l11111l11_opy_
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡴࡤࡪࠣࡴࡾࡺࡥࡴࡶࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࡬࡯ࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠻ࠢࠥᎣ") + str(e) + bstack1lll11l_opy_ (u"ࠤࠥᎤ"))
    def bstack1l1ll111111_opy_(self):
        bstack11llll1lll_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack11llll1lll_opy_, dict):
            if cli.config_observability:
                bstack11llll1lll_opy_.update(
                    {bstack1lll11l_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥᎥ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1lll11l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢᎦ") in accessibility.get(bstack1lll11l_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᎧ"), {}):
                    bstack1l11ll11lll_opy_ = accessibility.get(bstack1lll11l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᎨ"))
                    bstack1l11ll11lll_opy_.update({ bstack1lll11l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠣᎩ"): bstack1l11ll11lll_opy_.pop(bstack1lll11l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡢࡸࡴࡥࡷࡳࡣࡳࠦᎪ")) })
                bstack11llll1lll_opy_.update({bstack1lll11l_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᎫ"): accessibility })
        return bstack11llll1lll_opy_
    @measure(event_name=EVENTS.bstack1l1l11l1l1l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1l1l11ll1ll_opy_(self, bstack1l1l111l111_opy_: str = None, bstack1l1l111ll11_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1llll11l11l_opy_:
            return
        bstack11ll11l1l_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l111l111_opy_:
            req.bstack1l1l111l111_opy_ = bstack1l1l111l111_opy_
        if bstack1l1l111ll11_opy_:
            req.bstack1l1l111ll11_opy_ = bstack1l1l111ll11_opy_
        try:
            r = self.bstack1llll11l11l_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡷࡳࡵࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦᎬ"), datetime.now() - bstack11ll11l1l_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack111l1l1l1l_opy_(self, key: str, value: timedelta):
        tag = bstack1lll11l_opy_ (u"ࠦࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᎭ") if self.bstack1l1111lll_opy_() else bstack1lll11l_opy_ (u"ࠧࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᎮ")
        self.bstack1l1l1lll1ll_opy_[bstack1lll11l_opy_ (u"ࠨ࠺ࠣᎯ").join([tag + bstack1lll11l_opy_ (u"ࠢ࠮ࠤᎰ") + str(id(self)), key])] += value
    def bstack1111l1111_opy_(self):
        if not os.getenv(bstack1lll11l_opy_ (u"ࠣࡆࡈࡆ࡚ࡍ࡟ࡑࡇࡕࡊࠧᎱ"), bstack1lll11l_opy_ (u"ࠤ࠳ࠦᎲ")) == bstack1lll11l_opy_ (u"ࠥ࠵ࠧᎳ"):
            return
        bstack1l1l1l11lll_opy_ = dict()
        bstack1llll111ll1_opy_ = []
        if self.test_framework:
            bstack1llll111ll1_opy_.extend(list(self.test_framework.bstack1llll111ll1_opy_.values()))
        if self.bstack1lllll11lll_opy_:
            bstack1llll111ll1_opy_.extend(list(self.bstack1lllll11lll_opy_.bstack1llll111ll1_opy_.values()))
        for instance in bstack1llll111ll1_opy_:
            if not instance.platform_index in bstack1l1l1l11lll_opy_:
                bstack1l1l1l11lll_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l1l11lll_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll111ll_opy_().items():
                report[k] += v
                report[k.split(bstack1lll11l_opy_ (u"ࠦ࠿ࠨᎴ"))[0]] += v
        bstack1l11ll1l1l1_opy_ = sorted([(k, v) for k, v in self.bstack1l1l1lll1ll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l1llll1l_opy_ = 0
        for r in bstack1l11ll1l1l1_opy_:
            bstack1l1l11l1lll_opy_ = r[1].total_seconds()
            bstack1l1l1llll1l_opy_ += bstack1l1l11l1lll_opy_
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡾࡶࡠ࠶࡝ࡾ࠿ࠥᎵ") + str(bstack1l1l11l1lll_opy_) + bstack1lll11l_opy_ (u"ࠨࠢᎶ"))
        self.logger.debug(bstack1lll11l_opy_ (u"ࠢ࠮࠯ࠥᎷ"))
        bstack1l1l111l1l1_opy_ = []
        for platform_index, report in bstack1l1l1l11lll_opy_.items():
            bstack1l1l111l1l1_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l111l1l1_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll111l1_opy_ = set()
        bstack1l1l11ll11l_opy_ = 0
        for r in bstack1l1l111l1l1_opy_:
            bstack1l1l11l1lll_opy_ = r[2].total_seconds()
            bstack1l1l11ll11l_opy_ += bstack1l1l11l1lll_opy_
            bstack1lll111l1_opy_.add(r[0])
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡶࡨࡷࡹࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭࠮ࡽࡵ࡟࠵ࡣࡽ࠻ࡽࡵ࡟࠶ࡣࡽ࠾ࠤᎸ") + str(bstack1l1l11l1lll_opy_) + bstack1lll11l_opy_ (u"ࠤࠥᎹ"))
        if self.bstack1l1111lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥ࠱࠲ࠨᎺ"))
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻ࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠾ࡽࡷࡳࡹࡧ࡬ࡠࡥ࡯࡭ࢂࠦࡴࡦࡵࡷ࠾ࡵࡲࡡࡵࡨࡲࡶࡲࡹ࠭ࡼࡵࡷࡶ࠭ࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠪࡿࡀࠦᎻ") + str(bstack1l1l11ll11l_opy_) + bstack1lll11l_opy_ (u"ࠧࠨᎼ"))
        else:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠿ࠥᎽ") + str(bstack1l1l1llll1l_opy_) + bstack1lll11l_opy_ (u"ࠢࠣᎾ"))
        self.logger.debug(bstack1lll11l_opy_ (u"ࠣ࠯࠰ࠦᎿ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1llll11l11l_opy_:
            self.logger.error(bstack1lll11l_opy_ (u"ࠤࡦࡰ࡮ࡥࡳࡦࡴࡹ࡭ࡨ࡫ࠠࡪࡵࠣࡲࡴࡺࠠࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࡨ࠳ࠦࡃࡢࡰࡱࡳࡹࠦࡰࡦࡴࡩࡳࡷࡳࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨᏀ"))
            return None
        response = self.bstack1llll11l11l_opy_.TestOrchestration(request)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡸࡪࡹࡴ࠮ࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠮ࡵࡨࡷࡸ࡯࡯࡯࠿ࡾࢁࠧᏁ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l1l1llll_opy_(self, r):
        if r is not None and getattr(r, bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࠬᏂ"), None) and getattr(r.testhub, bstack1lll11l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬᏃ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1lll11l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᏄ")))
            for bstack1l11ll111ll_opy_, err in errors.items():
                if err[bstack1lll11l_opy_ (u"ࠧࡵࡻࡳࡩࠬᏅ")] == bstack1lll11l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭Ꮖ"):
                    self.logger.info(err[bstack1lll11l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᏇ")])
                else:
                    self.logger.error(err[bstack1lll11l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᏈ")])
    def bstack111lll111_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()