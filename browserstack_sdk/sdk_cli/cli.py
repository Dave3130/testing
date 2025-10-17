# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11lll11_opy_ import bstack1lll11ll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1llll1l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import bstack1l1l1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll11lll1_opy_ import bstack1l1ll1l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l11l11ll_opy_ import bstack1l1l11ll111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll111lll1_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1lll_opy_ import bstack1ll1llll111_opy_
from browserstack_sdk.sdk_cli.bstack1llll111ll1_opy_ import bstack1llll111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll11111l_opy_ import bstack1l11ll1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111ll_opy_ import bstack1l1l111ll_opy_, Events, bstack11l11ll11l_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1111l11_opy_ import bstack1l1l111111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lll11ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1ll1ll1_opy_
from bstack_utils.helper import Notset, bstack1l11lllll11_opy_, get_cli_dir, bstack1l1l111lll1_opy_, bstack11llll1l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll1l11l11l_opy_ import bstack1ll11l11111_opy_
from browserstack_sdk.sdk_cli.utils.bstack11lll1l1l_opy_ import bstack1l11l1ll1_opy_
from bstack_utils.helper import Notset, bstack1l11lllll11_opy_, get_cli_dir, bstack1l1l111lll1_opy_, bstack11llll1l11_opy_, bstack11ll11ll1l_opy_, bstack1l1111l1ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1l1ll_opy_, bstack1lll1ll1lll_opy_, bstack1lll1ll11ll_opy_, bstack1ll1111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1llllll1lll_opy_, bstack1lllll11111_opy_, bstack1llllllll1l_opy_
from bstack_utils.constants import *
from bstack_utils.bstack11l111l11l_opy_ import bstack11ll1l1l1_opy_
from bstack_utils import bstack1lll11ll11_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1llll1l111_opy_, bstack11l1l11l11_opy_
logger = bstack1lll11ll11_opy_.get_logger(__name__, bstack1lll11ll11_opy_.bstack1l1l1ll11ll_opy_())
def bstack1l1l11l1lll_opy_(bs_config):
    bstack1l1l1llll1l_opy_ = None
    bstack1l1l1llll11_opy_ = None
    try:
        bstack1l1l1llll11_opy_ = get_cli_dir()
        bstack1l1l1llll1l_opy_ = bstack1l1l111lll1_opy_(bstack1l1l1llll11_opy_)
        bstack1l1ll11l11l_opy_ = bstack1l11lllll11_opy_(bstack1l1l1llll1l_opy_, bstack1l1l1llll11_opy_, bs_config)
        bstack1l1l1llll1l_opy_ = bstack1l1ll11l11l_opy_ if bstack1l1ll11l11l_opy_ else bstack1l1l1llll1l_opy_
        if not bstack1l1l1llll1l_opy_:
            raise ValueError(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠧዘ"))
    except Exception as ex:
        logger.debug(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡺࡨࡦࠢ࡯ࡥࡹ࡫ࡳࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡾࢁࠧዙ").format(ex))
        bstack1l1l1llll1l_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠨዚ"))
        if bstack1l1l1llll1l_opy_:
            logger.debug(bstack11l111_opy_ (u"ࠦࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠢࡩࡶࡴࡳࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸ࠿ࠦࠢዛ") + str(bstack1l1l1llll1l_opy_) + bstack11l111_opy_ (u"ࠧࠨዜ"))
        else:
            logger.debug(bstack11l111_opy_ (u"ࠨࡎࡰࠢࡹࡥࡱ࡯ࡤࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷ࠿ࠥࡹࡥࡵࡷࡳࠤࡲࡧࡹࠡࡤࡨࠤ࡮ࡴࡣࡰ࡯ࡳࡰࡪࡺࡥ࠯ࠤዝ"))
    return bstack1l1l1llll1l_opy_, bstack1l1l1llll11_opy_
bstack1l1l1l1111l_opy_ = bstack11l111_opy_ (u"ࠢ࠺࠻࠼࠽ࠧዞ")
bstack1l11ll1lll1_opy_ = bstack11l111_opy_ (u"ࠣࡴࡨࡥࡩࡿࠢዟ")
bstack1l1l111l1ll_opy_ = bstack11l111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡖࡉࡘ࡙ࡉࡐࡐࡢࡍࡉࠨዠ")
bstack1l1l1lll11l_opy_ = bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡐࡎ࡙ࡔࡆࡐࡢࡅࡉࡊࡒࠣዡ")
bstack1l1111l11_opy_ = bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠢዢ")
bstack1l11ll1ll1l_opy_ = re.compile(bstack11l111_opy_ (u"ࡷࠨࠨࡀ࡫ࠬ࠲࠯࠮ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࢁࡈࡓࠪ࠰࠭ࠦዣ"))
bstack1l1l1l11lll_opy_ = bstack11l111_opy_ (u"ࠨࡤࡦࡸࡨࡰࡴࡶ࡭ࡦࡰࡷࠦዤ")
bstack1l1l1lll1l1_opy_ = bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡐࡔࡆࡉࡤࡌࡁࡍࡎࡅࡅࡈࡑࠢዥ")
bstack1l11lll1ll1_opy_ = [
    Events.bstack111ll1llll_opy_,
    Events.CONNECT,
    Events.bstack111l111ll_opy_,
]
class SDKCLI:
    _1ll1ll111ll_opy_ = None
    process: Union[None, Any]
    bstack1l11llll111_opy_: bool
    bstack1l1l11lll1l_opy_: bool
    bstack1l1l11111ll_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1l1ll11l1_opy_: Union[None, grpc.Channel]
    bstack1l11ll1ll11_opy_: str
    test_framework: TestFramework
    bstack1lllllll111_opy_: bstack1lll11ll11l_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l1ll1111_opy_: bstack1l11ll1l1ll_opy_
    accessibility: bstack1l1l1l1l1l1_opy_
    bstack11lll1l1l_opy_: bstack1l11l1ll1_opy_
    ai: bstack1l1ll1l11ll_opy_
    bstack1l1l1l11111_opy_: bstack1l1l11ll111_opy_
    bstack1l1l1ll111l_opy_: List[bstack1llll1l1l1l_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l11lll11l1_opy_: Any
    bstack1l1l1l1l11l_opy_: Dict[str, timedelta]
    bstack1l1l11l1l1l_opy_: str
    bstack1lll11lll11_opy_: bstack1lll11ll1ll_opy_
    def __new__(cls):
        if not cls._1ll1ll111ll_opy_:
            cls._1ll1ll111ll_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll111ll_opy_
    def __init__(self):
        self.process = None
        self.bstack1l11llll111_opy_ = False
        self.bstack1l1l1ll11l1_opy_ = None
        self.bstack1lllllllll1_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l1lll11l_opy_, None)
        self.bstack1l1l1l1l111_opy_ = os.environ.get(bstack1l1l111l1ll_opy_, bstack11l111_opy_ (u"ࠣࠤዦ")) == bstack11l111_opy_ (u"ࠤࠥዧ")
        self.bstack1l1l11lll1l_opy_ = False
        self.bstack1l1l11111ll_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l11lll11l1_opy_ = None
        self.test_framework = None
        self.bstack1lllllll111_opy_ = None
        self.bstack1l11ll1ll11_opy_=bstack11l111_opy_ (u"ࠥࠦየ")
        self.session_framework = None
        self.logger = bstack1lll11ll11_opy_.get_logger(self.__class__.__name__, bstack1lll11ll11_opy_.bstack1l1l1ll11ll_opy_())
        self.bstack1l1l1l1l11l_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11lll11_opy_ = bstack1lll11ll1ll_opy_()
        self.bstack1l1l11lll11_opy_ = None
        self.bstack1ll1lll11l1_opy_ = None
        self.bstack1l1l1ll1111_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l1ll111l_opy_ = []
    def bstack1ll1l1l1ll_opy_(self):
        return os.environ.get(bstack1l1111l11_opy_).lower().__eq__(bstack11l111_opy_ (u"ࠦࡹࡸࡵࡦࠤዩ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l1lll1l1_opy_, bstack11l111_opy_ (u"ࠬ࠭ዪ")).lower() in [bstack11l111_opy_ (u"࠭ࡴࡳࡷࡨࠫያ"), bstack11l111_opy_ (u"ࠧ࠲ࠩዬ"), bstack11l111_opy_ (u"ࠨࡻࡨࡷࠬይ")]:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡉࡳࡷࡩࡩ࡯ࡩࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡳ࡯ࡥࡧࠣࡨࡺ࡫ࠠࡵࡱࠣࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡓࡗࡉࡅࡠࡈࡄࡐࡑࡈࡁࡄࡍࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴࠡࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠥዮ"))
            os.environ[bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨዯ")] = bstack11l111_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥደ")
            return False
        if bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩዱ") in config and str(config[bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪዲ")]).lower() != bstack11l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ዳ"):
            return False
        bstack1l11ll1l1l1_opy_ = [bstack11l111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣዴ"), bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨድ")]
        bstack1l1l11l1111_opy_ = config.get(bstack11l111_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨዶ")) in bstack1l11ll1l1l1_opy_ or os.environ.get(bstack11l111_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬዷ")) in bstack1l11ll1l1l1_opy_
        os.environ[bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣዸ")] = str(bstack1l1l11l1111_opy_) # bstack1l1l11ll1ll_opy_ bstack1l1l111l1l1_opy_ VAR to bstack1l1l111llll_opy_ is binary running
        return bstack1l1l11l1111_opy_
    def bstack1l1l11l11_opy_(self):
        for event in bstack1l11lll1ll1_opy_:
            bstack1l1l111ll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l1l111ll_opy_.logger.debug(bstack11l111_opy_ (u"ࠨࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠥࡃ࠾ࠡࡽࡤࡶ࡬ࡹࡽࠡࠤዹ") + str(kwargs) + bstack11l111_opy_ (u"ࠢࠣዺ"))
            )
        bstack1l1l111ll_opy_.register(Events.bstack111ll1llll_opy_, self.__1l1l1l1l1ll_opy_)
        bstack1l1l111ll_opy_.register(Events.CONNECT, self.__1l1l1l111ll_opy_)
        bstack1l1l111ll_opy_.register(Events.bstack111l111ll_opy_, self.__1l1l1l1lll1_opy_)
        bstack1l1l111ll_opy_.register(Events.bstack11111ll1ll_opy_, self.__1l11lllll1l_opy_)
    def bstack1111ll1ll_opy_(self):
        return not self.bstack1l1l1l1l111_opy_ and os.environ.get(bstack1l1l111l1ll_opy_, bstack11l111_opy_ (u"ࠣࠤዻ")) != bstack11l111_opy_ (u"ࠤࠥዼ")
    def is_running(self):
        if self.bstack1l1l1l1l111_opy_:
            return self.bstack1l11llll111_opy_
        else:
            return bool(self.bstack1l1l1ll11l1_opy_)
    def bstack1l1l11l11l1_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l1ll111l_opy_) and cli.is_running()
    def __1l1l1l11ll1_opy_(self, bstack1l1l111ll11_opy_=10):
        if self.bstack1lllllllll1_opy_:
            return
        bstack1lll1l1ll1_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l1lll11l_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11l111_opy_ (u"ࠥ࡟ࠧዽ") + str(id(self)) + bstack11l111_opy_ (u"ࠦࡢࠦࡣࡰࡰࡱࡩࡨࡺࡩ࡯ࡩࠥዾ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11l111_opy_ (u"ࠧ࡭ࡲࡱࡥ࠱ࡩࡳࡧࡢ࡭ࡧࡢ࡬ࡹࡺࡰࡠࡲࡵࡳࡽࡿࠢዿ"), 0), (bstack11l111_opy_ (u"ࠨࡧࡳࡲࡦ࠲ࡪࡴࡡࡣ࡮ࡨࡣ࡭ࡺࡴࡱࡵࡢࡴࡷࡵࡸࡺࠤጀ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l111ll11_opy_)
        self.bstack1l1l1ll11l1_opy_ = channel
        self.bstack1lllllllll1_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1l1ll11l1_opy_)
        self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡩ࡯࡯ࡰࡨࡧࡹࠨጁ"), datetime.now() - bstack1lll1l1ll1_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l1lll11l_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦ࠽ࠤ࡮ࡹ࡟ࡤࡪ࡬ࡰࡩࡥࡰࡳࡱࡦࡩࡸࡹ࠽ࠣጂ") + str(self.bstack1111ll1ll_opy_()) + bstack11l111_opy_ (u"ࠤࠥጃ"))
    def __1l1l1l1lll1_opy_(self, event_name):
        if self.bstack1111ll1ll_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡸࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡃࡍࡋࠥጄ"))
        self.__1l11lll1l1l_opy_()
    def __1l11lllll1l_opy_(self, event_name, bstack1l1ll111l1l_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack11l111_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠦጅ"))
        bstack1l11lll11ll_opy_ = Path(bstack1lll1lll1ll_opy_ (u"ࠧࢁࡳࡦ࡮ࡩ࠲ࡨࡲࡩࡠࡦ࡬ࡶࢂ࠵ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࡳ࠯࡬ࡶࡳࡳࠨጆ"))
        if self.bstack1l1l1llll11_opy_ and bstack1l11lll11ll_opy_.exists():
            with open(bstack1l11lll11ll_opy_, bstack11l111_opy_ (u"࠭ࡲࠨጇ"), encoding=bstack11l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ገ")) as fp:
                data = json.load(fp)
                try:
                    bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"ࠨࡒࡒࡗ࡙࠭ጉ"), bstack11ll1l1l1_opy_(bstack11111lll11_opy_), data, {
                        bstack11l111_opy_ (u"ࠩࡤࡹࡹ࡮ࠧጊ"): (self.config[bstack11l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬጋ")], self.config[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧጌ")])
                    })
                except Exception as e:
                    logger.debug(bstack11l1l11l11_opy_.format(str(e)))
            bstack1l11lll11ll_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l1ll1lll_opy_, stage=STAGE.bstack1l111l11l_opy_)
    def __1l1l1l1l1ll_opy_(self, event_name: str, data):
        from bstack_utils.bstack1ll1111111_opy_ import bstack1lllll111l1_opy_
        self.bstack1l11ll1ll11_opy_, self.bstack1l1l1llll11_opy_ = bstack1l1l11l1lll_opy_(data.bs_config)
        os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡜ࡘࡉࡕࡃࡅࡐࡊࡥࡄࡊࡔࠪግ")] = self.bstack1l1l1llll11_opy_
        if not self.bstack1l11ll1ll11_opy_ or not self.bstack1l1l1llll11_opy_:
            raise ValueError(bstack11l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡵࡪࡨࠤࡘࡊࡋࠡࡅࡏࡍࠥࡨࡩ࡯ࡣࡵࡽࠧጎ"))
        if self.bstack1111ll1ll_opy_():
            self.__1l1l1l111ll_opy_(event_name, bstack11l11ll11l_opy_())
            return
        try:
            bstack1lllll111l1_opy_.end(EVENTS.bstack111llllll1_opy_.value, EVENTS.bstack111llllll1_opy_.value + bstack11l111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢጏ"), EVENTS.bstack111llllll1_opy_.value + bstack11l111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨጐ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11l111_opy_ (u"ࠤࡆࡳࡲࡶ࡬ࡦࡶࡨࠤࡘࡊࡋࠡࡕࡨࡸࡺࡶ࠮ࠣ጑"))
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࢀࢃࠢጒ").format(e))
        start = datetime.now()
        is_started = self.__1l1ll111lll_opy_()
        self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠦࡸࡶࡡࡸࡰࡢࡸ࡮ࡳࡥࠣጓ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l1l11ll1_opy_()
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࡥࡴࡪ࡯ࡨࠦጔ"), datetime.now() - start)
            start = datetime.now()
            self.__1l11llllll1_opy_(data)
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦጕ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l1l11l11_opy_, stage=STAGE.bstack1l111l11l_opy_)
    def __1l1l1l111ll_opy_(self, event_name: str, data: bstack11l11ll11l_opy_):
        if not self.bstack1111ll1ll_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡴ࡮ࡦࡥࡷ࠾ࠥࡴ࡯ࡵࠢࡤࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦ጖"))
            return
        bin_session_id = os.environ.get(bstack1l1l111l1ll_opy_)
        start = datetime.now()
        self.__1l1l1l11ll1_opy_()
        self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢ጗"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11l111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠥࡺ࡯ࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡇࡑࡏࠠࠣጘ") + str(bin_session_id) + bstack11l111_opy_ (u"ࠥࠦጙ"))
        start = datetime.now()
        self.__1l1ll1111l1_opy_()
        self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤጚ"), datetime.now() - start)
    def __1l1l11l1l11_opy_(self):
        if not self.bstack1lllllllll1_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࠡ࡯ࡲࡨࡺࡲࡥࡴࠤጛ"))
            return
        bstack1l1l111ll1l_opy_ = {
            bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥጜ"): (bstack1ll1llll111_opy_, bstack1llll111l1l_opy_, bstack1lll1ll1ll1_opy_),
            bstack11l111_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤጝ"): (bstack1llllll1111_opy_, bstack1lll11l1l11_opy_, bstack1lllllll1ll_opy_),
        }
        if not self.bstack1l1l11lll11_opy_ and self.session_framework in bstack1l1l111ll1l_opy_:
            bstack1l11llll11l_opy_, bstack1l1l11111l1_opy_, bstack1l1l11lllll_opy_ = bstack1l1l111ll1l_opy_[self.session_framework]
            bstack1l1l11ll1l1_opy_ = bstack1l1l11111l1_opy_()
            self.bstack1ll1lll11l1_opy_ = bstack1l1l11ll1l1_opy_
            self.bstack1l1l11lll11_opy_ = bstack1l1l11lllll_opy_
            self.bstack1l1l1ll111l_opy_.append(bstack1l1l11ll1l1_opy_)
            self.bstack1l1l1ll111l_opy_.append(bstack1l11llll11l_opy_(self.bstack1ll1lll11l1_opy_))
        if not self.bstack1l1l1ll1111_opy_ and self.config_observability and self.config_observability.success: # bstack111111l111_opy_
            self.bstack1l1l1ll1111_opy_ = bstack1l11ll1l1ll_opy_(self.bstack1l1l11lll11_opy_, self.bstack1ll1lll11l1_opy_) # bstack1l11ll1llll_opy_
            self.bstack1l1l1ll111l_opy_.append(self.bstack1l1l1ll1111_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l1l1l1l1_opy_(self.bstack1l1l11lll11_opy_, self.bstack1ll1lll11l1_opy_)
            self.bstack1l1l1ll111l_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11l111_opy_ (u"ࠣࡵࡨࡰ࡫ࡎࡥࡢ࡮ࠥጞ"), False) == True:
            self.ai = bstack1l1ll1l11ll_opy_()
            self.bstack1l1l1ll111l_opy_.append(self.ai)
        if not self.percy and self.bstack1l11lll11l1_opy_ and self.bstack1l11lll11l1_opy_.success:
            self.percy = bstack1l1l11ll111_opy_(self.bstack1l11lll11l1_opy_)
            self.bstack1l1l1ll111l_opy_.append(self.percy)
        for mod in self.bstack1l1l1ll111l_opy_:
            if not mod.bstack1lll11lll1l_opy_():
                mod.configure(self.bstack1lllllllll1_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11lll11_opy_)
    def __1l1l1lll111_opy_(self):
        for mod in self.bstack1l1l1ll111l_opy_:
            if mod.bstack1lll11lll1l_opy_():
                mod.configure(self.bstack1lllllllll1_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l11lll1lll_opy_, stage=STAGE.bstack1l111l11l_opy_)
    def __1l11llllll1_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l11lll1l_opy_:
            return
        self.__1l11lllllll_opy_(data)
        bstack1lll1l1ll1_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤጟ")
        req.sdk_language = bstack11l111_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥጠ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l11ll1ll1l_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡠࠨጡ") + str(id(self)) + bstack11l111_opy_ (u"ࠧࡣࠠ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦጢ"))
            r = self.bstack1lllllllll1_opy_.StartBinSession(req)
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺࡡࡳࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣጣ"), datetime.now() - bstack1lll1l1ll1_opy_)
            os.environ[bstack1l1l111l1ll_opy_] = r.bin_session_id
            self.__1l11llll1l1_opy_(r)
            self.__1l1l11l1l11_opy_()
            self.bstack1lll11lll11_opy_.start()
            self.bstack1l1l11lll1l_opy_ = True
            self.logger.debug(bstack11l111_opy_ (u"ࠢ࡜ࠤጤ") + str(id(self)) + bstack11l111_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠨጥ"))
        except grpc.bstack1l1l1ll1l1l_opy_ as bstack1l1l11l1ll1_opy_:
            self.logger.error(bstack11l111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦጦ") + str(bstack1l1l11l1ll1_opy_) + bstack11l111_opy_ (u"ࠥࠦጧ"))
            traceback.print_exc()
            raise bstack1l1l11l1ll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣጨ") + str(e) + bstack11l111_opy_ (u"ࠧࠨጩ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l111l111_opy_, stage=STAGE.bstack1l111l11l_opy_)
    def __1l1ll1111l1_opy_(self):
        if not self.bstack1111ll1ll_opy_() or not self.cli_bin_session_id or self.bstack1l1l11111ll_opy_:
            return
        bstack1lll1l1ll1_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ጪ"), bstack11l111_opy_ (u"ࠧ࠱ࠩጫ")))
        try:
            self.logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࠥጬ") + str(id(self)) + bstack11l111_opy_ (u"ࠤࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦጭ"))
            r = self.bstack1lllllllll1_opy_.ConnectBinSession(req)
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢጮ"), datetime.now() - bstack1lll1l1ll1_opy_)
            self.__1l11llll1l1_opy_(r)
            self.__1l1l11l1l11_opy_()
            self.bstack1lll11lll11_opy_.start()
            self.bstack1l1l11111ll_opy_ = True
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡠࠨጯ") + str(id(self)) + bstack11l111_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠦጰ"))
        except grpc.bstack1l1l1ll1l1l_opy_ as bstack1l1l11l1ll1_opy_:
            self.logger.error(bstack11l111_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡺࡩ࡮ࡧࡲࡩࡺࡺ࠭ࡦࡴࡵࡳࡷࡀࠠࠣጱ") + str(bstack1l1l11l1ll1_opy_) + bstack11l111_opy_ (u"ࠢࠣጲ"))
            traceback.print_exc()
            raise bstack1l1l11l1ll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧጳ") + str(e) + bstack11l111_opy_ (u"ࠤࠥጴ"))
            traceback.print_exc()
            raise e
    def __1l11llll1l1_opy_(self, r):
        self.bstack1l1l1llllll_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11l111_opy_ (u"ࠥࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡴࡧࡵࡺࡪࡸࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤጵ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11l111_opy_ (u"ࠦࡪࡳࡰࡵࡻࠣࡧࡴࡴࡦࡪࡩࠣࡪࡴࡻ࡮ࡥࠤጶ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡩࡷࡩࡹࠡ࡫ࡶࠤࡸ࡫࡮ࡵࠢࡲࡲࡱࡿࠠࡢࡵࠣࡴࡦࡸࡴࠡࡱࡩࠤࡹ࡮ࡥࠡࠤࡆࡳࡳࡴࡥࡤࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠲ࠢࠡࡣࡱࡨࠥࡺࡨࡪࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡣ࡯ࡷࡴࠦࡵࡴࡧࡧࠤࡧࡿࠠࡔࡶࡤࡶࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࡳࡧࡩࡳࡷ࡫ࠬࠡࡐࡲࡲࡪࠦࡨࡢࡰࡧࡰ࡮ࡴࡧࠡ࡫ࡶࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢጷ")
        self.bstack1l11lll11l1_opy_ = getattr(r, bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬጸ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫጹ")] = self.config_testhub.jwt
        os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ጺ")] = self.config_testhub.build_hashed_id
    def bstack1l11lll1l11_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l11llll111_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1l111l11l_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1l111l11l_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l11lll1l11_opy_(event_name=EVENTS.bstack1l1ll11l1ll_opy_, stage=STAGE.bstack1l111l11l_opy_)
    def __1l1ll111lll_opy_(self, bstack1l1l111ll11_opy_=10):
        if self.bstack1l11llll111_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡶࡸࡦࡸࡴ࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡶࡺࡴ࡮ࡪࡰࡪࠦጻ"))
            return True
        self.logger.debug(bstack11l111_opy_ (u"ࠥࡷࡹࡧࡲࡵࠤጼ"))
        if os.getenv(bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡆࡐ࡙ࠦጽ")) == bstack1l1l1l11lll_opy_:
            self.cli_bin_session_id = bstack1l1l1l11lll_opy_
            self.cli_listen_addr = bstack11l111_opy_ (u"ࠧࡻ࡮ࡪࡺ࠽࠳ࡹࡳࡰ࠰ࡵࡧ࡯࠲ࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࠦࡵ࠱ࡷࡴࡩ࡫ࠣጾ") % (self.cli_bin_session_id)
            self.bstack1l11llll111_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l11ll1ll11_opy_, bstack11l111_opy_ (u"ࠨࡳࡥ࡭ࠥጿ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1ll111ll1_opy_ compat for text=True in bstack1l1l1ll1ll1_opy_ python
            encoding=bstack11l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨፀ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1ll111l11_opy_ = threading.Thread(target=self.__1l1l11llll1_opy_, args=(bstack1l1l111ll11_opy_,))
        bstack1l1ll111l11_opy_.start()
        bstack1l1ll111l11_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡴࡲࡤࡻࡳࡀࠠࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࡁࢀࡹࡥ࡭ࡨ࠱ࡴࡷࡵࡣࡦࡵࡶ࠲ࡷ࡫ࡴࡶࡴࡱࡧࡴࡪࡥࡾࠢࡲࡹࡹࡃࡻࡴࡧ࡯ࡪ࠳ࡶࡲࡰࡥࡨࡷࡸ࠴ࡳࡵࡦࡲࡹࡹ࠴ࡲࡦࡣࡧࠬ࠮ࢃࠠࡦࡴࡵࡁࠧፁ") + str(self.process.stderr.read()) + bstack11l111_opy_ (u"ࠤࠥፂ"))
        if not self.bstack1l11llll111_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠥ࡟ࠧፃ") + str(id(self)) + bstack11l111_opy_ (u"ࠦࡢࠦࡣ࡭ࡧࡤࡲࡺࡶࠢፄ"))
            self.__1l11lll1l1l_opy_()
        self.logger.debug(bstack11l111_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡵࡸ࡯ࡤࡧࡶࡷࡤࡸࡥࡢࡦࡼ࠾ࠥࠨፅ") + str(self.bstack1l11llll111_opy_) + bstack11l111_opy_ (u"ࠨࠢፆ"))
        return self.bstack1l11llll111_opy_
    def __1l1l11llll1_opy_(self, bstack1l1ll11l1l1_opy_=10):
        bstack1l1l1l1ll1l_opy_ = time.time()
        while self.process and time.time() - bstack1l1l1l1ll1l_opy_ < bstack1l1ll11l1l1_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11l111_opy_ (u"ࠢࡪࡦࡀࠦፇ") in line:
                    self.cli_bin_session_id = line.split(bstack11l111_opy_ (u"ࠣ࡫ࡧࡁࠧፈ"))[-1:][0].strip()
                    self.logger.debug(bstack11l111_opy_ (u"ࠤࡦࡰ࡮ࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠺ࠣፉ") + str(self.cli_bin_session_id) + bstack11l111_opy_ (u"ࠥࠦፊ"))
                    continue
                if bstack11l111_opy_ (u"ࠦࡱ࡯ࡳࡵࡧࡱࡁࠧፋ") in line:
                    self.cli_listen_addr = line.split(bstack11l111_opy_ (u"ࠧࡲࡩࡴࡶࡨࡲࡂࠨፌ"))[-1:][0].strip()
                    self.logger.debug(bstack11l111_opy_ (u"ࠨࡣ࡭࡫ࡢࡰ࡮ࡹࡴࡦࡰࡢࡥࡩࡪࡲ࠻ࠤፍ") + str(self.cli_listen_addr) + bstack11l111_opy_ (u"ࠢࠣፎ"))
                    continue
                if bstack11l111_opy_ (u"ࠣࡲࡲࡶࡹࡃࠢፏ") in line:
                    port = line.split(bstack11l111_opy_ (u"ࠤࡳࡳࡷࡺ࠽ࠣፐ"))[-1:][0].strip()
                    self.logger.debug(bstack11l111_opy_ (u"ࠥࡴࡴࡸࡴ࠻ࠤፑ") + str(port) + bstack11l111_opy_ (u"ࠦࠧፒ"))
                    continue
                if line.strip() == bstack1l11ll1lll1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11l111_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡎࡕ࡟ࡔࡖࡕࡉࡆࡓࠢፓ"), bstack11l111_opy_ (u"ࠨ࠱ࠣፔ")) == bstack11l111_opy_ (u"ࠢ࠲ࠤፕ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l11llll111_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡧࡵࡶࡴࡸ࠺ࠡࠤፖ") + str(e) + bstack11l111_opy_ (u"ࠤࠥፗ"))
        return False
    @measure(event_name=EVENTS.bstack1l11llll1ll_opy_, stage=STAGE.bstack1l111l11l_opy_)
    def __1l11lll1l1l_opy_(self):
        if self.bstack1l1l1ll11l1_opy_:
            self.bstack1lll11lll11_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l1ll1l11_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l11111ll_opy_:
                    self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠥࡷࡹࡵࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢፘ"), datetime.now() - start)
                else:
                    self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠦࡸࡺ࡯ࡱࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣፙ"), datetime.now() - start)
            self.__1l1l1lll111_opy_()
            start = datetime.now()
            self.bstack1l1l1ll11l1_opy_.close()
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠧࡪࡩࡴࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢፚ"), datetime.now() - start)
            self.bstack1l1l1ll11l1_opy_ = None
        if self.process:
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡳࡵࡱࡳࠦ፛"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠢ࡬࡫࡯ࡰࡤࡺࡩ࡮ࡧࠥ፜"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l1l1l111_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1111l1ll1l_opy_()
                self.logger.info(
                    bstack11l111_opy_ (u"ࠣࡘ࡬ࡷ࡮ࡺࠠࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠣ፝").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11l111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨ፞")] = self.config_testhub.build_hashed_id
        self.bstack1l11llll111_opy_ = False
    def __1l11lllllll_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11l111_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ፟")] = selenium.__version__
            data.frameworks.append(bstack11l111_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ፠"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack11l111_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ፡")] = __version__
            data.frameworks.append(bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ።"))
        except:
            pass
    def bstack1l1l1111l1l_opy_(self, hub_url: str, platform_index: int, bstack1ll11l1111_opy_: Any):
        if self.bstack1lllllll111_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡸ࡫ࡴࠡࡷࡳࠦ፣"))
            return
        try:
            bstack1lll1l1ll1_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11l111_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ፤")
            self.bstack1lllllll111_opy_ = bstack1lllllll1ll_opy_(
                cli.config.get(bstack11l111_opy_ (u"ࠤ࡫ࡹࡧ࡛ࡲ࡭ࠤ፥"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1lllll1llll_opy_={bstack11l111_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡢࡳࡵࡺࡩࡰࡰࡶࡣ࡫ࡸ࡯࡮ࡡࡦࡥࡵࡹࠢ፦"): bstack1ll11l1111_opy_}
            )
            def bstack1l11lll1111_opy_(self):
                return
            if self.config.get(bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠨ፧"), True):
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
            WebDriver.upload_attachment = staticmethod(bstack1l11l1ll1_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11l11111_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ፨"), datetime.now() - bstack1lll1l1ll1_opy_)
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡵࡨࡰࡪࡴࡩࡶ࡯࠽ࠤࠧ፩") + str(e) + bstack11l111_opy_ (u"ࠢࠣ፪"))
    def bstack1l1ll1111ll_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1llllll1l1_opy_
            self.bstack1lllllll111_opy_ = bstack1lll1ll1ll1_opy_(
                platform_index,
                framework_name=bstack11l111_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ፫"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠻ࠢࠥ፬") + str(e) + bstack11l111_opy_ (u"ࠥࠦ፭"))
            pass
    def bstack1l1l1l1ll11_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡳࡦࡶࠣࡹࡵࠨ፮"))
            return
        if bstack11llll1l11_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ፯"): pytest.__version__ }, [bstack11l111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥ፰")], self.bstack1lll11lll11_opy_, self.bstack1lllllllll1_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l1l111111l_opy_({ bstack11l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢ፱"): pytest.__version__ }, [bstack11l111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣ፲")], self.bstack1lll11lll11_opy_, self.bstack1lllllllll1_opy_)
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࠨ፳") + str(e) + bstack11l111_opy_ (u"ࠥࠦ፴"))
        self.bstack1l1l1lll1ll_opy_()
    def bstack1l1l1lll1ll_opy_(self):
        if not self.bstack1ll1l1l1ll_opy_():
            return
        bstack111llll1l_opy_ = None
        def bstack1ll111lll1_opy_(config, startdir):
            return bstack11l111_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤ፵").format(bstack11l111_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦ፶"))
        def bstack1ll11lll1l_opy_():
            return
        def bstack11111l11l1_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11l111_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭፷"):
                return bstack11l111_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ፸")
            else:
                return bstack111llll1l_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack111llll1l_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1ll111lll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll11lll1l_opy_
            Config.getoption = bstack11111l11l1_opy_
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡴࡤࡪࠣࡴࡾࡺࡥࡴࡶࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࡬࡯ࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠻ࠢࠥ፹") + str(e) + bstack11l111_opy_ (u"ࠤࠥ፺"))
    def bstack1l1l1111ll1_opy_(self):
        bstack1ll1ll11ll_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1ll1ll11ll_opy_, dict):
            if cli.config_observability:
                bstack1ll1ll11ll_opy_.update(
                    {bstack11l111_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥ፻"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢ፼") in accessibility.get(bstack11l111_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨ፽"), {}):
                    bstack1l1l1l1llll_opy_ = accessibility.get(bstack11l111_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢ፾"))
                    bstack1l1l1l1llll_opy_.update({ bstack11l111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠣ፿"): bstack1l1l1l1llll_opy_.pop(bstack11l111_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡢࡸࡴࡥࡷࡳࡣࡳࠦᎀ")) })
                bstack1ll1ll11ll_opy_.update({bstack11l111_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᎁ"): accessibility })
        return bstack1ll1ll11ll_opy_
    @measure(event_name=EVENTS.bstack1l1ll11l111_opy_, stage=STAGE.bstack1l111l11l_opy_)
    def bstack1l1l1ll1l11_opy_(self, bstack1l1l1l111l1_opy_: str = None, bstack1l1l1l11l1l_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1lllllllll1_opy_:
            return
        bstack1lll1l1ll1_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1l111l1_opy_:
            req.bstack1l1l1l111l1_opy_ = bstack1l1l1l111l1_opy_
        if bstack1l1l1l11l1l_opy_:
            req.bstack1l1l1l11l1l_opy_ = bstack1l1l1l11l1l_opy_
        try:
            r = self.bstack1lllllllll1_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡷࡳࡵࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦᎂ"), datetime.now() - bstack1lll1l1ll1_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1llll1l11l_opy_(self, key: str, value: timedelta):
        tag = bstack11l111_opy_ (u"ࠦࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᎃ") if self.bstack1111ll1ll_opy_() else bstack11l111_opy_ (u"ࠧࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᎄ")
        self.bstack1l1l1l1l11l_opy_[bstack11l111_opy_ (u"ࠨ࠺ࠣᎅ").join([tag + bstack11l111_opy_ (u"ࠢ࠮ࠤᎆ") + str(id(self)), key])] += value
    def bstack1111l1ll1l_opy_(self):
        if not os.getenv(bstack11l111_opy_ (u"ࠣࡆࡈࡆ࡚ࡍ࡟ࡑࡇࡕࡊࠧᎇ"), bstack11l111_opy_ (u"ࠤ࠳ࠦᎈ")) == bstack11l111_opy_ (u"ࠥ࠵ࠧᎉ"):
            return
        bstack1l1l1lllll1_opy_ = dict()
        bstack1lll1l11lll_opy_ = []
        if self.test_framework:
            bstack1lll1l11lll_opy_.extend(list(self.test_framework.bstack1lll1l11lll_opy_.values()))
        if self.bstack1lllllll111_opy_:
            bstack1lll1l11lll_opy_.extend(list(self.bstack1lllllll111_opy_.bstack1lll1l11lll_opy_.values()))
        for instance in bstack1lll1l11lll_opy_:
            if not instance.platform_index in bstack1l1l1lllll1_opy_:
                bstack1l1l1lllll1_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l1lllll1_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll1ll11_opy_().items():
                report[k] += v
                report[k.split(bstack11l111_opy_ (u"ࠦ࠿ࠨᎊ"))[0]] += v
        bstack1l1l11ll11l_opy_ = sorted([(k, v) for k, v in self.bstack1l1l1l1l11l_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l1111111_opy_ = 0
        for r in bstack1l1l11ll11l_opy_:
            bstack1l1l1111lll_opy_ = r[1].total_seconds()
            bstack1l1l1111111_opy_ += bstack1l1l1111lll_opy_
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡾࡶࡠ࠶࡝ࡾ࠿ࠥᎋ") + str(bstack1l1l1111lll_opy_) + bstack11l111_opy_ (u"ࠨࠢᎌ"))
        self.logger.debug(bstack11l111_opy_ (u"ࠢ࠮࠯ࠥᎍ"))
        bstack1l11lll111l_opy_ = []
        for platform_index, report in bstack1l1l1lllll1_opy_.items():
            bstack1l11lll111l_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l11lll111l_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll11lll_opy_ = set()
        bstack1l1l11l111l_opy_ = 0
        for r in bstack1l11lll111l_opy_:
            bstack1l1l1111lll_opy_ = r[2].total_seconds()
            bstack1l1l11l111l_opy_ += bstack1l1l1111lll_opy_
            bstack1lll11lll_opy_.add(r[0])
            self.logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡶࡨࡷࡹࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭࠮ࡽࡵ࡟࠵ࡣࡽ࠻ࡽࡵ࡟࠶ࡣࡽ࠾ࠤᎎ") + str(bstack1l1l1111lll_opy_) + bstack11l111_opy_ (u"ࠤࠥᎏ"))
        if self.bstack1111ll1ll_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠥ࠱࠲ࠨ᎐"))
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻ࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠾ࡽࡷࡳࡹࡧ࡬ࡠࡥ࡯࡭ࢂࠦࡴࡦࡵࡷ࠾ࡵࡲࡡࡵࡨࡲࡶࡲࡹ࠭ࡼࡵࡷࡶ࠭ࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠪࡿࡀࠦ᎑") + str(bstack1l1l11l111l_opy_) + bstack11l111_opy_ (u"ࠧࠨ᎒"))
        else:
            self.logger.debug(bstack11l111_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠿ࠥ᎓") + str(bstack1l1l1111111_opy_) + bstack11l111_opy_ (u"ࠢࠣ᎔"))
        self.logger.debug(bstack11l111_opy_ (u"ࠣ࠯࠰ࠦ᎕"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1lllllllll1_opy_:
            self.logger.error(bstack11l111_opy_ (u"ࠤࡦࡰ࡮ࡥࡳࡦࡴࡹ࡭ࡨ࡫ࠠࡪࡵࠣࡲࡴࡺࠠࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࡨ࠳ࠦࡃࡢࡰࡱࡳࡹࠦࡰࡦࡴࡩࡳࡷࡳࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨ᎖"))
            return None
        response = self.bstack1lllllllll1_opy_.TestOrchestration(request)
        self.logger.debug(bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴ࠮ࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠮ࡵࡨࡷࡸ࡯࡯࡯࠿ࡾࢁࠧ᎗").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l1llllll_opy_(self, r):
        if r is not None and getattr(r, bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࠬ᎘"), None) and getattr(r.testhub, bstack11l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ᎙"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧ᎚")))
            for bstack1l1ll111111_opy_, err in errors.items():
                if err[bstack11l111_opy_ (u"ࠧࡵࡻࡳࡩࠬ᎛")] == bstack11l111_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭᎜"):
                    self.logger.info(err[bstack11l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ᎝")])
                else:
                    self.logger.error(err[bstack11l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᎞")])
    def bstack1l1l111lll_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()