# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import bstack1l1l11lllll_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll1l1111_opy_ import bstack1l1ll1l1lll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1lll111_opy_ import bstack1l11llll111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll11_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll1l1_opy_ import bstack1ll1lll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1llll11llll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1111lll_opy_ import bstack1l11llllll1_opy_
from browserstack_sdk.sdk_cli.bstack111ll111l1_opy_ import bstack111ll111l1_opy_, Events, bstack1l111l11l_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l11l1l1l_opy_ import bstack1l1l1l111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lll111ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1llll11l1ll_opy_
from bstack_utils.helper import Notset, bstack1l1l1l11l11_opy_, get_cli_dir, bstack1l11ll1ll1l_opy_, bstack1ll11111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll11l1ll1l_opy_ import bstack1ll1l1ll111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1lll1ll_opy_ import bstack11ll1llll1_opy_
from bstack_utils.helper import Notset, bstack1l1l1l11l11_opy_, get_cli_dir, bstack1l11ll1ll1l_opy_, bstack1ll11111l1_opy_, bstack1l11l1ll1l_opy_, bstack11lll111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111lll_opy_, bstack1lll1lll1l1_opy_, bstack1lll1lll11l_opy_, bstack1ll111lll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_, bstack1llll1ll111_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1l1l11llll_opy_ import bstack11ll11l11_opy_
from bstack_utils import bstack11111ll111_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11111l1ll_opy_, bstack1lll111ll_opy_
logger = bstack11111ll111_opy_.get_logger(__name__, bstack11111ll111_opy_.bstack1l1l1lll11l_opy_())
def bstack1l1l1llllll_opy_(bs_config):
    bstack1l1ll11l1l1_opy_ = None
    bstack1l1ll1111ll_opy_ = None
    try:
        bstack1l1ll1111ll_opy_ = get_cli_dir()
        bstack1l1ll11l1l1_opy_ = bstack1l11ll1ll1l_opy_(bstack1l1ll1111ll_opy_)
        bstack1l1l11ll1ll_opy_ = bstack1l1l1l11l11_opy_(bstack1l1ll11l1l1_opy_, bstack1l1ll1111ll_opy_, bs_config)
        bstack1l1ll11l1l1_opy_ = bstack1l1l11ll1ll_opy_ if bstack1l1l11ll1ll_opy_ else bstack1l1ll11l1l1_opy_
        if not bstack1l1ll11l1l1_opy_:
            raise ValueError(bstack111111l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠦዞ"))
    except Exception as ex:
        logger.debug(bstack111111l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡹ࡮ࡥࠡ࡮ࡤࡸࡪࡹࡴࠡࡤ࡬ࡲࡦࡸࡹࠡࡽࢀࠦዟ").format(ex))
        bstack1l1ll11l1l1_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠧዠ"))
        if bstack1l1ll11l1l1_opy_:
            logger.debug(bstack111111l_opy_ (u"ࠥࡊࡦࡲ࡬ࡪࡰࡪࠤࡧࡧࡣ࡬ࠢࡷࡳ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠡࡨࡵࡳࡲࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷ࠾ࠥࠨዡ") + str(bstack1l1ll11l1l1_opy_) + bstack111111l_opy_ (u"ࠦࠧዢ"))
        else:
            logger.debug(bstack111111l_opy_ (u"ࠧࡔ࡯ࠡࡸࡤࡰ࡮ࡪࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥ࡫࡮ࡷ࡫ࡵࡳࡳࡳࡥ࡯ࡶ࠾ࠤࡸ࡫ࡴࡶࡲࠣࡱࡦࡿࠠࡣࡧࠣ࡭ࡳࡩ࡯࡮ࡲ࡯ࡩࡹ࡫࠮ࠣዣ"))
    return bstack1l1ll11l1l1_opy_, bstack1l1ll1111ll_opy_
bstack1l1l11llll1_opy_ = bstack111111l_opy_ (u"ࠨ࠹࠺࠻࠼ࠦዤ")
bstack1l11ll1lll1_opy_ = bstack111111l_opy_ (u"ࠢࡳࡧࡤࡨࡾࠨዥ")
bstack1l1ll11ll1l_opy_ = bstack111111l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧዦ")
bstack1l1ll111l11_opy_ = bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡏࡍࡘ࡚ࡅࡏࡡࡄࡈࡉࡘࠢዧ")
bstack1l11l11lll_opy_ = bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨየ")
bstack1l1l11l11l1_opy_ = re.compile(bstack111111l_opy_ (u"ࡶࠧ࠮࠿ࡪࠫ࠱࠮࠭ࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࢀࡇ࡙ࠩ࠯ࠬࠥዩ"))
bstack1l1l1l11111_opy_ = bstack111111l_opy_ (u"ࠧࡪࡥࡷࡧ࡯ࡳࡵࡳࡥ࡯ࡶࠥዪ")
bstack1l1l1l11lll_opy_ = bstack111111l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡏࡓࡅࡈࡣࡋࡇࡌࡍࡄࡄࡇࡐࠨያ")
bstack1l11lll111l_opy_ = [
    Events.bstack1l11l1llll_opy_,
    Events.CONNECT,
    Events.bstack11l1l11l1_opy_,
]
class SDKCLI:
    _1ll1ll1l111_opy_ = None
    process: Union[None, Any]
    bstack1l1l11ll111_opy_: bool
    bstack1l1l1ll1ll1_opy_: bool
    bstack1l1l1l1llll_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l11lll11l1_opy_: Union[None, grpc.Channel]
    bstack1l1ll111111_opy_: str
    test_framework: TestFramework
    bstack1lllllllll1_opy_: bstack1lll111ll1l_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l111l1l1_opy_: bstack1l11llllll1_opy_
    accessibility: bstack1l1l11lllll_opy_
    bstack1ll1lll1ll_opy_: bstack11ll1llll1_opy_
    ai: bstack1l1ll1l1lll_opy_
    bstack1l11lll1lll_opy_: bstack1l11llll111_opy_
    bstack1l1l111lll1_opy_: List[bstack1llllll111l_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l1l1ll11_opy_: Any
    bstack1l1ll111lll_opy_: Dict[str, timedelta]
    bstack1l1l1ll1lll_opy_: str
    bstack1lll11lllll_opy_: bstack1lll11llll1_opy_
    def __new__(cls):
        if not cls._1ll1ll1l111_opy_:
            cls._1ll1ll1l111_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll1l111_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1l11ll111_opy_ = False
        self.bstack1l11lll11l1_opy_ = None
        self.bstack111111111l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1ll111l11_opy_, None)
        self.bstack1l1l111ll11_opy_ = os.environ.get(bstack1l1ll11ll1l_opy_, bstack111111l_opy_ (u"ࠢࠣዬ")) == bstack111111l_opy_ (u"ࠣࠤይ")
        self.bstack1l1l1ll1ll1_opy_ = False
        self.bstack1l1l1l1llll_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l1l1ll11_opy_ = None
        self.test_framework = None
        self.bstack1lllllllll1_opy_ = None
        self.bstack1l1ll111111_opy_=bstack111111l_opy_ (u"ࠤࠥዮ")
        self.session_framework = None
        self.logger = bstack11111ll111_opy_.get_logger(self.__class__.__name__, bstack11111ll111_opy_.bstack1l1l1lll11l_opy_())
        self.bstack1l1ll111lll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11lllll_opy_ = bstack1lll11llll1_opy_()
        self.bstack1l1l11l1lll_opy_ = None
        self.bstack1ll1lllll11_opy_ = None
        self.bstack1l1l111l1l1_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l111lll1_opy_ = []
    def bstack11l1l1l1ll_opy_(self):
        return os.environ.get(bstack1l11l11lll_opy_).lower().__eq__(bstack111111l_opy_ (u"ࠥࡸࡷࡻࡥࠣዯ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l1l11lll_opy_, bstack111111l_opy_ (u"ࠫࠬደ")).lower() in [bstack111111l_opy_ (u"ࠬࡺࡲࡶࡧࠪዱ"), bstack111111l_opy_ (u"࠭࠱ࠨዲ"), bstack111111l_opy_ (u"ࠧࡺࡧࡶࠫዳ")]:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡈࡲࡶࡨ࡯࡮ࡨࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡲࡵࡤࡦࠢࡧࡹࡪࠦࡴࡰࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡒࡖࡈࡋ࡟ࡇࡃࡏࡐࡇࡇࡃࡌࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺࠠࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠤዴ"))
            os.environ[bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡋࡖࡣࡗ࡛ࡎࡏࡋࡑࡋࠧድ")] = bstack111111l_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤዶ")
            return False
        if bstack111111l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨዷ") in config and str(config[bstack111111l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩዸ")]).lower() != bstack111111l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬዹ"):
            return False
        bstack1l1l111ll1l_opy_ = [bstack111111l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢዺ"), bstack111111l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧዻ")]
        bstack1l1l11ll1l1_opy_ = config.get(bstack111111l_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧዼ")) in bstack1l1l111ll1l_opy_ or os.environ.get(bstack111111l_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫዽ")) in bstack1l1l111ll1l_opy_
        os.environ[bstack111111l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡍࡘࡥࡒࡖࡐࡑࡍࡓࡍࠢዾ")] = str(bstack1l1l11ll1l1_opy_) # bstack1l1l1ll111l_opy_ bstack1l1l11111l1_opy_ VAR to bstack1l1l1ll11l1_opy_ is binary running
        return bstack1l1l11ll1l1_opy_
    def bstack11111llll_opy_(self):
        for event in bstack1l11lll111l_opy_:
            bstack111ll111l1_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack111ll111l1_opy_.logger.debug(bstack111111l_opy_ (u"ࠧࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠤࡂࡄࠠࡼࡣࡵ࡫ࡸࢃࠠࠣዿ") + str(kwargs) + bstack111111l_opy_ (u"ࠨࠢጀ"))
            )
        bstack111ll111l1_opy_.register(Events.bstack1l11l1llll_opy_, self.__1l1l11lll1l_opy_)
        bstack111ll111l1_opy_.register(Events.CONNECT, self.__1l1l1111l1l_opy_)
        bstack111ll111l1_opy_.register(Events.bstack11l1l11l1_opy_, self.__1l1l1lll1l1_opy_)
        bstack111ll111l1_opy_.register(Events.bstack1llllllll1_opy_, self.__1l1l1l1lll1_opy_)
    def bstack1111lllll_opy_(self):
        return not self.bstack1l1l111ll11_opy_ and os.environ.get(bstack1l1ll11ll1l_opy_, bstack111111l_opy_ (u"ࠢࠣጁ")) != bstack111111l_opy_ (u"ࠣࠤጂ")
    def is_running(self):
        if self.bstack1l1l111ll11_opy_:
            return self.bstack1l1l11ll111_opy_
        else:
            return bool(self.bstack1l11lll11l1_opy_)
    def bstack1l1l1lll1ll_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l111lll1_opy_) and cli.is_running()
    def __1l1ll11111l_opy_(self, bstack1l1ll11l1ll_opy_=10):
        if self.bstack111111111l_opy_:
            return
        bstack1111ll111_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1ll111l11_opy_, self.cli_listen_addr)
        self.logger.debug(bstack111111l_opy_ (u"ࠤ࡞ࠦጃ") + str(id(self)) + bstack111111l_opy_ (u"ࠥࡡࠥࡩ࡯࡯ࡰࡨࡧࡹ࡯࡮ࡨࠤጄ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack111111l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠰ࡨࡲࡦࡨ࡬ࡦࡡ࡫ࡸࡹࡶ࡟ࡱࡴࡲࡼࡾࠨጅ"), 0), (bstack111111l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠱ࡩࡳࡧࡢ࡭ࡧࡢ࡬ࡹࡺࡰࡴࡡࡳࡶࡴࡾࡹࠣጆ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1ll11l1ll_opy_)
        self.bstack1l11lll11l1_opy_ = channel
        self.bstack111111111l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l11lll11l1_opy_)
        self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡨࡵ࡮࡯ࡧࡦࡸࠧጇ"), datetime.now() - bstack1111ll111_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1ll111l11_opy_] = self.cli_listen_addr
        self.logger.debug(bstack111111l_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥ࠼ࠣ࡭ࡸࡥࡣࡩ࡫࡯ࡨࡤࡶࡲࡰࡥࡨࡷࡸࡃࠢገ") + str(self.bstack1111lllll_opy_()) + bstack111111l_opy_ (u"ࠣࠤጉ"))
    def __1l1l1lll1l1_opy_(self, event_name):
        if self.bstack1111lllll_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡷࡹࡵࡰࡱ࡫ࡱ࡫ࠥࡉࡌࡊࠤጊ"))
        self.__1l11lll1l11_opy_()
    def __1l1l1l1lll1_opy_(self, event_name, bstack1l11ll1ll11_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack111111l_opy_ (u"ࠥࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠥጋ"))
        bstack1l1l111111l_opy_ = Path(bstack1llll1ll1_opy_ (u"ࠦࢀࡹࡥ࡭ࡨ࠱ࡧࡱ࡯࡟ࡥ࡫ࡵࢁ࠴ࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࡹ࠮࡫ࡵࡲࡲࠧጌ"))
        if self.bstack1l1ll1111ll_opy_ and bstack1l1l111111l_opy_.exists():
            with open(bstack1l1l111111l_opy_, bstack111111l_opy_ (u"ࠬࡸࠧግ"), encoding=bstack111111l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬጎ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠧࡑࡑࡖࡘࠬጏ"), bstack11ll11l11_opy_(bstack111llllll_opy_), data, {
                        bstack111111l_opy_ (u"ࠨࡣࡸࡸ࡭࠭ጐ"): (self.config[bstack111111l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ጑")], self.config[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ጒ")])
                    })
                except Exception as e:
                    logger.debug(bstack1lll111ll_opy_.format(str(e)))
            bstack1l1l111111l_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l1ll1l1l_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1l1l11lll1l_opy_(self, event_name: str, data):
        from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
        self.bstack1l1ll111111_opy_, self.bstack1l1ll1111ll_opy_ = bstack1l1l1llllll_opy_(data.bs_config)
        os.environ[bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡛ࡗࡏࡔࡂࡄࡏࡉࡤࡊࡉࡓࠩጓ")] = self.bstack1l1ll1111ll_opy_
        if not self.bstack1l1ll111111_opy_ or not self.bstack1l1ll1111ll_opy_:
            raise ValueError(bstack111111l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡴࡩࡧࠣࡗࡉࡑࠠࡄࡎࡌࠤࡧ࡯࡮ࡢࡴࡼࠦጔ"))
        if self.bstack1111lllll_opy_():
            self.__1l1l1111l1l_opy_(event_name, bstack1l111l11l_opy_())
            return
        try:
            bstack1llllll1lll_opy_.end(EVENTS.bstack111ll11111_opy_.value, EVENTS.bstack111ll11111_opy_.value + bstack111111l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨጕ"), EVENTS.bstack111ll11111_opy_.value + bstack111111l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ጖"), status=True, failure=None, test_name=None)
            logger.debug(bstack111111l_opy_ (u"ࠣࡅࡲࡱࡵࡲࡥࡵࡧࠣࡗࡉࡑࠠࡔࡧࡷࡹࡵ࠴ࠢ጗"))
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵࠣࡿࢂࠨጘ").format(e))
        start = datetime.now()
        is_started = self.__1l11lll1111_opy_()
        self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥࡷࡵࡧࡷ࡯ࡡࡷ࡭ࡲ࡫ࠢጙ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1ll11111l_opy_()
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥጚ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1ll11l11l_opy_(data)
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥጛ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l111l1ll_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1l1l1111l1l_opy_(self, event_name: str, data: bstack1l111l11l_opy_):
        if not self.bstack1111lllll_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦࡳࡳࡴࡥࡤࡶ࠽ࠤࡳࡵࡴࠡࡣࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࠥጜ"))
            return
        bin_session_id = os.environ.get(bstack1l1ll11ll1l_opy_)
        start = datetime.now()
        self.__1l1ll11111l_opy_()
        self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨጝ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack111111l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠤࡹࡵࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢࡆࡐࡎࠦࠢጞ") + str(bin_session_id) + bstack111111l_opy_ (u"ࠤࠥጟ"))
        start = datetime.now()
        self.__1l1l1l111l1_opy_()
        self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣጠ"), datetime.now() - start)
    def __1l1l1l1l1ll_opy_(self):
        if not self.bstack111111111l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡨࡧ࡮࡯ࡱࡷࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࠠ࡮ࡱࡧࡹࡱ࡫ࡳࠣጡ"))
            return
        bstack1l11lllllll_opy_ = {
            bstack111111l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤጢ"): (bstack1ll1lll1ll1_opy_, bstack1llll11llll_opy_, bstack1llll11l1ll_opy_),
            bstack111111l_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣጣ"): (bstack1lllll111l1_opy_, bstack1lll11l11l1_opy_, bstack1llllll11ll_opy_),
        }
        if not self.bstack1l1l11l1lll_opy_ and self.session_framework in bstack1l11lllllll_opy_:
            bstack1l1l1lllll1_opy_, bstack1l1l1111ll1_opy_, bstack1l1l1l1l111_opy_ = bstack1l11lllllll_opy_[self.session_framework]
            bstack1l1l1111l11_opy_ = bstack1l1l1111ll1_opy_()
            self.bstack1ll1lllll11_opy_ = bstack1l1l1111l11_opy_
            self.bstack1l1l11l1lll_opy_ = bstack1l1l1l1l111_opy_
            self.bstack1l1l111lll1_opy_.append(bstack1l1l1111l11_opy_)
            self.bstack1l1l111lll1_opy_.append(bstack1l1l1lllll1_opy_(self.bstack1ll1lllll11_opy_))
        if not self.bstack1l1l111l1l1_opy_ and self.config_observability and self.config_observability.success: # bstack1llll1l1l1l_opy_
            self.bstack1l1l111l1l1_opy_ = bstack1l11llllll1_opy_(self.bstack1l1l11l1lll_opy_, self.bstack1ll1lllll11_opy_) # bstack1l1l11l1111_opy_
            self.bstack1l1l111lll1_opy_.append(self.bstack1l1l111l1l1_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l11lllll_opy_(self.bstack1l1l11l1lll_opy_, self.bstack1ll1lllll11_opy_)
            self.bstack1l1l111lll1_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack111111l_opy_ (u"ࠢࡴࡧ࡯ࡪࡍ࡫ࡡ࡭ࠤጤ"), False) == True:
            self.ai = bstack1l1ll1l1lll_opy_()
            self.bstack1l1l111lll1_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l1l1ll11_opy_ and self.bstack1l1l1l1ll11_opy_.success:
            self.percy = bstack1l11llll111_opy_(self.bstack1l1l1l1ll11_opy_)
            self.bstack1l1l111lll1_opy_.append(self.percy)
        for mod in self.bstack1l1l111lll1_opy_:
            if not mod.bstack1lll1l11111_opy_():
                mod.configure(self.bstack111111111l_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11lllll_opy_)
    def __1l1l11111ll_opy_(self):
        for mod in self.bstack1l1l111lll1_opy_:
            if mod.bstack1lll1l11111_opy_():
                mod.configure(self.bstack111111111l_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l11llll1l1_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1l1ll11l11l_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l1ll1ll1_opy_:
            return
        self.__1l1l11l11ll_opy_(data)
        bstack1111ll111_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack111111l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣጥ")
        req.sdk_language = bstack111111l_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤጦ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l11l11l1_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack111111l_opy_ (u"ࠥ࡟ࠧጧ") + str(id(self)) + bstack111111l_opy_ (u"ࠦࡢࠦ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡳࡵࡣࡵࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥጨ"))
            r = self.bstack111111111l_opy_.StartBinSession(req)
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡹࡧࡲࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢጩ"), datetime.now() - bstack1111ll111_opy_)
            os.environ[bstack1l1ll11ll1l_opy_] = r.bin_session_id
            self.__1l1l1ll11ll_opy_(r)
            self.__1l1l1l1l1ll_opy_()
            self.bstack1lll11lllll_opy_.start()
            self.bstack1l1l1ll1ll1_opy_ = True
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡛ࠣጪ") + str(id(self)) + bstack111111l_opy_ (u"ࠢ࡞ࠢࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠧጫ"))
        except grpc.bstack1l11lll1l1l_opy_ as bstack1l1l1l11ll1_opy_:
            self.logger.error(bstack111111l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡵ࡫ࡰࡩࡴ࡫ࡵࡵ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥጬ") + str(bstack1l1l1l11ll1_opy_) + bstack111111l_opy_ (u"ࠤࠥጭ"))
            traceback.print_exc()
            raise bstack1l1l1l11ll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢጮ") + str(e) + bstack111111l_opy_ (u"ࠦࠧጯ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11llll1ll_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1l1l1l111l1_opy_(self):
        if not self.bstack1111lllll_opy_() or not self.cli_bin_session_id or self.bstack1l1l1l1llll_opy_:
            return
        bstack1111ll111_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬጰ"), bstack111111l_opy_ (u"࠭࠰ࠨጱ")))
        try:
            self.logger.debug(bstack111111l_opy_ (u"ࠢ࡜ࠤጲ") + str(id(self)) + bstack111111l_opy_ (u"ࠣ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥጳ"))
            r = self.bstack111111111l_opy_.ConnectBinSession(req)
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡤࡱࡱࡲࡪࡩࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨጴ"), datetime.now() - bstack1111ll111_opy_)
            self.__1l1l1ll11ll_opy_(r)
            self.__1l1l1l1l1ll_opy_()
            self.bstack1lll11lllll_opy_.start()
            self.bstack1l1l1l1llll_opy_ = True
            self.logger.debug(bstack111111l_opy_ (u"ࠥ࡟ࠧጵ") + str(id(self)) + bstack111111l_opy_ (u"ࠦࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦࠥጶ"))
        except grpc.bstack1l11lll1l1l_opy_ as bstack1l1l1l11ll1_opy_:
            self.logger.error(bstack111111l_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡹ࡯࡭ࡦࡱࡨࡹࡹ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢጷ") + str(bstack1l1l1l11ll1_opy_) + bstack111111l_opy_ (u"ࠨࠢጸ"))
            traceback.print_exc()
            raise bstack1l1l1l11ll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦጹ") + str(e) + bstack111111l_opy_ (u"ࠣࠤጺ"))
            traceback.print_exc()
            raise e
    def __1l1l1ll11ll_opy_(self, r):
        self.bstack1l1ll11l111_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack111111l_opy_ (u"ࠤࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡳࡦࡴࡹࡩࡷࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣጻ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack111111l_opy_ (u"ࠥࡩࡲࡶࡴࡺࠢࡦࡳࡳ࡬ࡩࡨࠢࡩࡳࡺࡴࡤࠣጼ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack111111l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡨࡶࡨࡿࠠࡪࡵࠣࡷࡪࡴࡴࠡࡱࡱࡰࡾࠦࡡࡴࠢࡳࡥࡷࡺࠠࡰࡨࠣࡸ࡭࡫ࠠࠣࡅࡲࡲࡳ࡫ࡣࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲ࠱ࠨࠠࡢࡰࡧࠤࡹ࡮ࡩࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤ࡮ࡹࠠࡢ࡮ࡶࡳࠥࡻࡳࡦࡦࠣࡦࡾࠦࡓࡵࡣࡵࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࡲࡦࡨࡲࡶࡪ࠲ࠠࡏࡱࡱࡩࠥ࡮ࡡ࡯ࡦ࡯࡭ࡳ࡭ࠠࡪࡵࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨጽ")
        self.bstack1l1l1l1ll11_opy_ = getattr(r, bstack111111l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫጾ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪጿ")] = self.config_testhub.jwt
        os.environ[bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬፀ")] = self.config_testhub.build_hashed_id
    def bstack1l1l1l1ll1l_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1l11ll111_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1ll1111l1_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1ll1111l1_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1l1l1ll1l_opy_(event_name=EVENTS.bstack1l1l1l1111l_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1l11lll1111_opy_(self, bstack1l1ll11l1ll_opy_=10):
        if self.bstack1l1l11ll111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡵࡷࡥࡷࡺ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡵࡹࡳࡴࡩ࡯ࡩࠥፁ"))
            return True
        self.logger.debug(bstack111111l_opy_ (u"ࠤࡶࡸࡦࡸࡴࠣፂ"))
        if os.getenv(bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡅࡏࡘࠥፃ")) == bstack1l1l1l11111_opy_:
            self.cli_bin_session_id = bstack1l1l1l11111_opy_
            self.cli_listen_addr = bstack111111l_opy_ (u"ࠦࡺࡴࡩࡹ࠼࠲ࡸࡲࡶ࠯ࡴࡦ࡮࠱ࡵࡲࡡࡵࡨࡲࡶࡲ࠳ࠥࡴ࠰ࡶࡳࡨࡱࠢፄ") % (self.cli_bin_session_id)
            self.bstack1l1l11ll111_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1ll111111_opy_, bstack111111l_opy_ (u"ࠧࡹࡤ࡬ࠤፅ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l11l1l11_opy_ compat for text=True in bstack1l1ll111l1l_opy_ python
            encoding=bstack111111l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧፆ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1l1llll1l_opy_ = threading.Thread(target=self.__1l1l11lll11_opy_, args=(bstack1l1ll11l1ll_opy_,))
        bstack1l1l1llll1l_opy_.start()
        bstack1l1l1llll1l_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack111111l_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡳࡱࡣࡺࡲ࠿ࠦࡲࡦࡶࡸࡶࡳࡩ࡯ࡥࡧࡀࡿࡸ࡫࡬ࡧ࠰ࡳࡶࡴࡩࡥࡴࡵ࠱ࡶࡪࡺࡵࡳࡰࡦࡳࡩ࡫ࡽࠡࡱࡸࡸࡂࢁࡳࡦ࡮ࡩ࠲ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡹࡴࡥࡱࡸࡸ࠳ࡸࡥࡢࡦࠫ࠭ࢂࠦࡥࡳࡴࡀࠦፇ") + str(self.process.stderr.read()) + bstack111111l_opy_ (u"ࠣࠤፈ"))
        if not self.bstack1l1l11ll111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠤ࡞ࠦፉ") + str(id(self)) + bstack111111l_opy_ (u"ࠥࡡࠥࡩ࡬ࡦࡣࡱࡹࡵࠨፊ"))
            self.__1l11lll1l11_opy_()
        self.logger.debug(bstack111111l_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡴࡷࡵࡣࡦࡵࡶࡣࡷ࡫ࡡࡥࡻ࠽ࠤࠧፋ") + str(self.bstack1l1l11ll111_opy_) + bstack111111l_opy_ (u"ࠧࠨፌ"))
        return self.bstack1l1l11ll111_opy_
    def __1l1l11lll11_opy_(self, bstack1l11lllll11_opy_=10):
        bstack1l1ll11lll1_opy_ = time.time()
        while self.process and time.time() - bstack1l1ll11lll1_opy_ < bstack1l11lllll11_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack111111l_opy_ (u"ࠨࡩࡥ࠿ࠥፍ") in line:
                    self.cli_bin_session_id = line.split(bstack111111l_opy_ (u"ࠢࡪࡦࡀࠦፎ"))[-1:][0].strip()
                    self.logger.debug(bstack111111l_opy_ (u"ࠣࡥ࡯࡭ࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡀࠢፏ") + str(self.cli_bin_session_id) + bstack111111l_opy_ (u"ࠤࠥፐ"))
                    continue
                if bstack111111l_opy_ (u"ࠥࡰ࡮ࡹࡴࡦࡰࡀࠦፑ") in line:
                    self.cli_listen_addr = line.split(bstack111111l_opy_ (u"ࠦࡱ࡯ࡳࡵࡧࡱࡁࠧፒ"))[-1:][0].strip()
                    self.logger.debug(bstack111111l_opy_ (u"ࠧࡩ࡬ࡪࡡ࡯࡭ࡸࡺࡥ࡯ࡡࡤࡨࡩࡸ࠺ࠣፓ") + str(self.cli_listen_addr) + bstack111111l_opy_ (u"ࠨࠢፔ"))
                    continue
                if bstack111111l_opy_ (u"ࠢࡱࡱࡵࡸࡂࠨፕ") in line:
                    port = line.split(bstack111111l_opy_ (u"ࠣࡲࡲࡶࡹࡃࠢፖ"))[-1:][0].strip()
                    self.logger.debug(bstack111111l_opy_ (u"ࠤࡳࡳࡷࡺ࠺ࠣፗ") + str(port) + bstack111111l_opy_ (u"ࠥࠦፘ"))
                    continue
                if line.strip() == bstack1l11ll1lll1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack111111l_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡍࡔࡥࡓࡕࡔࡈࡅࡒࠨፙ"), bstack111111l_opy_ (u"ࠧ࠷ࠢፚ")) == bstack111111l_opy_ (u"ࠨ࠱ࠣ፛"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1l11ll111_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack111111l_opy_ (u"ࠢࡦࡴࡵࡳࡷࡀࠠࠣ፜") + str(e) + bstack111111l_opy_ (u"ࠣࠤ፝"))
        return False
    @measure(event_name=EVENTS.bstack1l1ll111ll1_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1l11lll1l11_opy_(self):
        if self.bstack1l11lll11l1_opy_:
            self.bstack1lll11lllll_opy_.stop()
            start = datetime.now()
            if self.bstack1l1ll11ll11_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l1l1llll_opy_:
                    self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠤࡶࡸࡴࡶ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨ፞"), datetime.now() - start)
                else:
                    self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥࡷࡹࡵࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢ፟"), datetime.now() - start)
            self.__1l1l11111ll_opy_()
            start = datetime.now()
            self.bstack1l11lll11l1_opy_.close()
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠦࡩ࡯ࡳࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨ፠"), datetime.now() - start)
            self.bstack1l11lll11l1_opy_ = None
        if self.process:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡹࡴࡰࡲࠥ፡"))
            start = datetime.now()
            self.process.terminate()
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠨ࡫ࡪ࡮࡯ࡣࡹ࡯࡭ࡦࠤ።"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l111ll11_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack11lll111l_opy_()
                self.logger.info(
                    bstack111111l_opy_ (u"ࠢࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠢ፣").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack111111l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧ፤")] = self.config_testhub.build_hashed_id
        self.bstack1l1l11ll111_opy_ = False
    def __1l1l11l11ll_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack111111l_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦ፥")] = selenium.__version__
            data.frameworks.append(bstack111111l_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ፦"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack111111l_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ፧")] = __version__
            data.frameworks.append(bstack111111l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ፨"))
        except:
            pass
    def bstack1l1l1l1l1l1_opy_(self, hub_url: str, platform_index: int, bstack111l111l1l_opy_: Any):
        if self.bstack1lllllllll1_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠠࡴࡧࡷࡹࡵࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡷࡪࡺࠠࡶࡲࠥ፩"))
            return
        try:
            bstack1111ll111_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack111111l_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤ፪")
            self.bstack1lllllllll1_opy_ = bstack1llllll11ll_opy_(
                cli.config.get(bstack111111l_opy_ (u"ࠣࡪࡸࡦ࡚ࡸ࡬ࠣ፫"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll1l1lll_opy_={bstack111111l_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨ፬"): bstack111l111l1l_opy_}
            )
            def bstack1l1l1l11l1l_opy_(self):
                return
            if self.config.get(bstack111111l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠧ፭"), True):
                Service.start = bstack1l1l1l11l1l_opy_
                Service.stop = bstack1l1l1l11l1l_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack11ll1llll1_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll1l1ll111_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ፮"), datetime.now() - bstack1111ll111_opy_)
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠼ࠣࠦ፯") + str(e) + bstack111111l_opy_ (u"ࠨࠢ፰"))
    def bstack1l1l1ll1111_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1l1l1lll1l_opy_
            self.bstack1lllllllll1_opy_ = bstack1llll11l1ll_opy_(
                platform_index,
                framework_name=bstack111111l_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ፱"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠺ࠡࠤ፲") + str(e) + bstack111111l_opy_ (u"ࠤࠥ፳"))
            pass
    def bstack1l1l1llll11_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack111111l_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠤࡸ࡫ࡴࡶࡲࠣࡴࡾࡺࡥࡴࡶ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡹࡥࡵࠢࡸࡴࠧ፴"))
            return
        if bstack1ll11111l1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack111111l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦ፵"): pytest.__version__ }, [bstack111111l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤ፶")], self.bstack1lll11lllll_opy_, self.bstack111111111l_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l1l1l111ll_opy_({ bstack111111l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨ፷"): pytest.__version__ }, [bstack111111l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢ፸")], self.bstack1lll11lllll_opy_, self.bstack111111111l_opy_)
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡾࡺࡥࡴࡶ࠽ࠤࠧ፹") + str(e) + bstack111111l_opy_ (u"ࠤࠥ፺"))
        self.bstack1l11llll11l_opy_()
    def bstack1l11llll11l_opy_(self):
        if not self.bstack11l1l1l1ll_opy_():
            return
        bstack1ll1lll1l1_opy_ = None
        def bstack111l1llll_opy_(config, startdir):
            return bstack111111l_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀ࠶ࡽࠣ፻").format(bstack111111l_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥ፼"))
        def bstack11llll1lll_opy_():
            return
        def bstack111l1lll1_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack111111l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬ፽"):
                return bstack111111l_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧ፾")
            else:
                return bstack1ll1lll1l1_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1ll1lll1l1_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack111l1llll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11llll1lll_opy_
            Config.getoption = bstack111l1lll1_opy_
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡺࡣࡩࠢࡳࡽࡹ࡫ࡳࡵࠢࡶࡩࡱ࡫࡮ࡪࡷࡰࠤ࡫ࡵࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠺ࠡࠤ፿") + str(e) + bstack111111l_opy_ (u"ࠣࠤᎀ"))
    def bstack1l11lll11ll_opy_(self):
        bstack111ll1111_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack111ll1111_opy_, dict):
            if cli.config_observability:
                bstack111ll1111_opy_.update(
                    {bstack111111l_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤᎁ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack111111l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࡤࡺ࡯ࡠࡹࡵࡥࡵࠨᎂ") in accessibility.get(bstack111111l_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᎃ"), {}):
                    bstack1l1l1ll1l11_opy_ = accessibility.get(bstack111111l_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᎄ"))
                    bstack1l1l1ll1l11_opy_.update({ bstack111111l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡕࡱ࡚ࡶࡦࡶࠢᎅ"): bstack1l1l1ll1l11_opy_.pop(bstack111111l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡡࡷࡳࡤࡽࡲࡢࡲࠥᎆ")) })
                bstack111ll1111_opy_.update({bstack111111l_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᎇ"): accessibility })
        return bstack111ll1111_opy_
    @measure(event_name=EVENTS.bstack1l1l11ll11l_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1l1ll11ll11_opy_(self, bstack1l1l1l1l11l_opy_: str = None, bstack1l1l111llll_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack111111111l_opy_:
            return
        bstack1111ll111_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1l1l11l_opy_:
            req.bstack1l1l1l1l11l_opy_ = bstack1l1l1l1l11l_opy_
        if bstack1l1l111llll_opy_:
            req.bstack1l1l111llll_opy_ = bstack1l1l111llll_opy_
        try:
            r = self.bstack111111111l_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡶࡲࡴࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥᎈ"), datetime.now() - bstack1111ll111_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack11l1l1lll_opy_(self, key: str, value: timedelta):
        tag = bstack111111l_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࠥᎉ") if self.bstack1111lllll_opy_() else bstack111111l_opy_ (u"ࠦࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵࠥᎊ")
        self.bstack1l1ll111lll_opy_[bstack111111l_opy_ (u"ࠧࡀࠢᎋ").join([tag + bstack111111l_opy_ (u"ࠨ࠭ࠣᎌ") + str(id(self)), key])] += value
    def bstack11lll111l_opy_(self):
        if not os.getenv(bstack111111l_opy_ (u"ࠢࡅࡇࡅ࡙ࡌࡥࡐࡆࡔࡉࠦᎍ"), bstack111111l_opy_ (u"ࠣ࠲ࠥᎎ")) == bstack111111l_opy_ (u"ࠤ࠴ࠦᎏ"):
            return
        bstack1l1l111l11l_opy_ = dict()
        bstack1llll111l1l_opy_ = []
        if self.test_framework:
            bstack1llll111l1l_opy_.extend(list(self.test_framework.bstack1llll111l1l_opy_.values()))
        if self.bstack1lllllllll1_opy_:
            bstack1llll111l1l_opy_.extend(list(self.bstack1lllllllll1_opy_.bstack1llll111l1l_opy_.values()))
        for instance in bstack1llll111l1l_opy_:
            if not instance.platform_index in bstack1l1l111l11l_opy_:
                bstack1l1l111l11l_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l111l11l_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll1lll1_opy_().items():
                report[k] += v
                report[k.split(bstack111111l_opy_ (u"ࠥ࠾ࠧ᎐"))[0]] += v
        bstack1l11ll1llll_opy_ = sorted([(k, v) for k, v in self.bstack1l1ll111lll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l11l111l_opy_ = 0
        for r in bstack1l11ll1llll_opy_:
            bstack1l1l11l1ll1_opy_ = r[1].total_seconds()
            bstack1l1l11l111l_opy_ += bstack1l1l11l1ll1_opy_
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻ࡽࡵ࡟࠵ࡣࡽ࠾ࠤ᎑") + str(bstack1l1l11l1ll1_opy_) + bstack111111l_opy_ (u"ࠧࠨ᎒"))
        self.logger.debug(bstack111111l_opy_ (u"ࠨ࠭࠮ࠤ᎓"))
        bstack1l1l1111111_opy_ = []
        for platform_index, report in bstack1l1l111l11l_opy_.items():
            bstack1l1l1111111_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l1111111_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll1l111_opy_ = set()
        bstack1l11lll1ll1_opy_ = 0
        for r in bstack1l1l1111111_opy_:
            bstack1l1l11l1ll1_opy_ = r[2].total_seconds()
            bstack1l11lll1ll1_opy_ += bstack1l1l11l1ll1_opy_
            bstack1lll1l111_opy_.add(r[0])
            self.logger.debug(bstack111111l_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡵࡧࡶࡸ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࡼࡴ࡞࠴ࡢࢃ࠺ࡼࡴ࡞࠵ࡢࢃ࠽ࠣ᎔") + str(bstack1l1l11l1ll1_opy_) + bstack111111l_opy_ (u"ࠣࠤ᎕"))
        if self.bstack1111lllll_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠤ࠰࠱ࠧ᎖"))
            self.logger.debug(bstack111111l_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡧࡱ࡯࠺ࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠽ࡼࡶࡲࡸࡦࡲ࡟ࡤ࡮࡬ࢁࠥࡺࡥࡴࡶ࠽ࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠳ࡻࡴࡶࡵࠬࡵࡲࡡࡵࡨࡲࡶࡲࡹࠩࡾ࠿ࠥ᎗") + str(bstack1l11lll1ll1_opy_) + bstack111111l_opy_ (u"ࠦࠧ᎘"))
        else:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠾ࠤ᎙") + str(bstack1l1l11l111l_opy_) + bstack111111l_opy_ (u"ࠨࠢ᎚"))
        self.logger.debug(bstack111111l_opy_ (u"ࠢ࠮࠯ࠥ᎛"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, bstack1l11lllll1l_opy_: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            bstack1l11lllll1l_opy_=bstack1l11lllll1l_opy_
        )
        if not self.bstack111111111l_opy_:
            self.logger.error(bstack111111l_opy_ (u"ࠣࡥ࡯࡭ࡤࡹࡥࡳࡸ࡬ࡧࡪࠦࡩࡴࠢࡱࡳࡹࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࡧ࠲ࠥࡉࡡ࡯ࡰࡲࡸࠥࡶࡥࡳࡨࡲࡶࡲࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧ᎜"))
            return None
        response = self.bstack111111111l_opy_.TestOrchestration(request)
        self.logger.debug(bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺ࠭ࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠭ࡴࡧࡶࡷ࡮ࡵ࡮࠾ࡽࢀࠦ᎝").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1ll11l111_opy_(self, r):
        if r is not None and getattr(r, bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࠫ᎞"), None) and getattr(r.testhub, bstack111111l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ᎟"), None):
            errors = json.loads(r.testhub.errors.decode(bstack111111l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᎠ")))
            for bstack1l1l111l111_opy_, err in errors.items():
                if err[bstack111111l_opy_ (u"࠭ࡴࡺࡲࡨࠫᎡ")] == bstack111111l_opy_ (u"ࠧࡪࡰࡩࡳࠬᎢ"):
                    self.logger.info(err[bstack111111l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᎣ")])
                else:
                    self.logger.error(err[bstack111111l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᎤ")])
    def bstack1l111ll1l1_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()