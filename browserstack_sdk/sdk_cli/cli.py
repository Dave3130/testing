# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll111llll_opy_ import bstack1lll11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1lll1_opy_ import bstack1l1l11l1lll_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll1111l1_opy_ import bstack1l1ll111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1lll111_opy_ import bstack1l11lll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import bstack1llll11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1lll11111l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll11ll1_opy_ import bstack1ll1ll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1lll11l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1l11lll_opy_ import bstack1l1l1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1llll11l_opy_ import bstack1l1llll11l_opy_, Events, bstack1l1ll11ll_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1lll11l_opy_ import bstack1l11lll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1lll1111l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l11l_opy_ import bstack1lll11l1l11_opy_
from bstack_utils.helper import Notset, bstack1l1l111l1l1_opy_, get_cli_dir, bstack1l11ll11l11_opy_, bstack1llllll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll11l11l1l_opy_ import bstack1ll11llll11_opy_
from browserstack_sdk.sdk_cli.utils.bstack11ll1111l_opy_ import bstack1lll1l1ll1_opy_
from bstack_utils.helper import Notset, bstack1l1l111l1l1_opy_, get_cli_dir, bstack1l11ll11l11_opy_, bstack1llllll1l1_opy_, bstack11ll11ll1l_opy_, bstack1ll11ll111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l111l1_opy_, bstack1lll1l1l1ll_opy_, bstack1lll1ll1ll1_opy_, bstack1l1llll111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1llll111l1l_opy_, bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1l1lll1lll_opy_ import bstack11l1l1l1l1_opy_
from bstack_utils import bstack11111l1ll1_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1111ll11l_opy_, bstack1l1l1ll1l_opy_
logger = bstack11111l1ll1_opy_.get_logger(__name__, bstack11111l1ll1_opy_.bstack1l1l1ll111l_opy_())
def bstack1l11llll111_opy_(bs_config):
    bstack1l11lll1l1l_opy_ = None
    bstack1l1l1llllll_opy_ = None
    try:
        bstack1l1l1llllll_opy_ = get_cli_dir()
        bstack1l11lll1l1l_opy_ = bstack1l11ll11l11_opy_(bstack1l1l1llllll_opy_)
        bstack1l11ll1ll1l_opy_ = bstack1l1l111l1l1_opy_(bstack1l11lll1l1l_opy_, bstack1l1l1llllll_opy_, bs_config)
        bstack1l11lll1l1l_opy_ = bstack1l11ll1ll1l_opy_ if bstack1l11ll1ll1l_opy_ else bstack1l11lll1l1l_opy_
        if not bstack1l11lll1l1l_opy_:
            raise ValueError(bstack11ll1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠦጝ"))
    except Exception as ex:
        logger.debug(bstack11ll1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡹ࡮ࡥࠡ࡮ࡤࡸࡪࡹࡴࠡࡤ࡬ࡲࡦࡸࡹࠡࡽࢀࠦጞ").format(ex))
        bstack1l11lll1l1l_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠧጟ"))
        if bstack1l11lll1l1l_opy_:
            logger.debug(bstack11ll1ll_opy_ (u"ࠥࡊࡦࡲ࡬ࡪࡰࡪࠤࡧࡧࡣ࡬ࠢࡷࡳ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠡࡨࡵࡳࡲࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷ࠾ࠥࠨጠ") + str(bstack1l11lll1l1l_opy_) + bstack11ll1ll_opy_ (u"ࠦࠧጡ"))
        else:
            logger.debug(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࠡࡸࡤࡰ࡮ࡪࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥ࡫࡮ࡷ࡫ࡵࡳࡳࡳࡥ࡯ࡶ࠾ࠤࡸ࡫ࡴࡶࡲࠣࡱࡦࡿࠠࡣࡧࠣ࡭ࡳࡩ࡯࡮ࡲ࡯ࡩࡹ࡫࠮ࠣጢ"))
    return bstack1l11lll1l1l_opy_, bstack1l1l1llllll_opy_
bstack1l11ll1111l_opy_ = bstack11ll1ll_opy_ (u"ࠨ࠹࠺࠻࠼ࠦጣ")
bstack1l11llll1l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡳࡧࡤࡨࡾࠨጤ")
bstack1l1l1ll1l11_opy_ = bstack11ll1ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧጥ")
bstack1l1l1ll1lll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡏࡍࡘ࡚ࡅࡏࡡࡄࡈࡉࡘࠢጦ")
bstack1l1ll11l11_opy_ = bstack11ll1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨጧ")
bstack1l1l111lll1_opy_ = re.compile(bstack11ll1ll_opy_ (u"ࡶࠧ࠮࠿ࡪࠫ࠱࠮࠭ࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࢀࡇ࡙ࠩ࠯ࠬࠥጨ"))
bstack1l1l1111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠧࡪࡥࡷࡧ࡯ࡳࡵࡳࡥ࡯ࡶࠥጩ")
bstack1l11lllll1l_opy_ = bstack11ll1ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡏࡓࡅࡈࡣࡋࡇࡌࡍࡄࡄࡇࡐࠨጪ")
bstack1l1l1llll1l_opy_ = [
    Events.bstack111l1111ll_opy_,
    Events.CONNECT,
    Events.bstack11lll1ll1l_opy_,
]
class SDKCLI:
    _1ll1l1lll1l_opy_ = None
    process: Union[None, Any]
    bstack1l1l11l111l_opy_: bool
    bstack1l1l1l1ll11_opy_: bool
    bstack1l1l11ll1l1_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l11ll11lll_opy_: Union[None, grpc.Channel]
    bstack1l11ll1llll_opy_: str
    test_framework: TestFramework
    bstack1llll1lll1l_opy_: bstack1lll1111l11_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l1ll1111_opy_: bstack1l1l1l1l1l1_opy_
    accessibility: bstack1l1l11l1lll_opy_
    bstack11ll1111l_opy_: bstack1lll1l1ll1_opy_
    ai: bstack1l1ll111l1l_opy_
    bstack1l1l1l11111_opy_: bstack1l11lll11ll_opy_
    bstack1l1l1l1l111_opy_: List[bstack1lllll111l1_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l1l1ll1l_opy_: Any
    bstack1l1l11ll1ll_opy_: Dict[str, timedelta]
    bstack1l11l1llll1_opy_: str
    bstack1lll111llll_opy_: bstack1lll11l111l_opy_
    def __new__(cls):
        if not cls._1ll1l1lll1l_opy_:
            cls._1ll1l1lll1l_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1l1lll1l_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1l11l111l_opy_ = False
        self.bstack1l11ll11lll_opy_ = None
        self.bstack1llllll1l1l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l1ll1lll_opy_, None)
        self.bstack1l11ll111ll_opy_ = os.environ.get(bstack1l1l1ll1l11_opy_, bstack11ll1ll_opy_ (u"ࠢࠣጫ")) == bstack11ll1ll_opy_ (u"ࠣࠤጬ")
        self.bstack1l1l1l1ll11_opy_ = False
        self.bstack1l1l11ll1l1_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l1l1ll1l_opy_ = None
        self.test_framework = None
        self.bstack1llll1lll1l_opy_ = None
        self.bstack1l11ll1llll_opy_=bstack11ll1ll_opy_ (u"ࠤࠥጭ")
        self.session_framework = None
        self.logger = bstack11111l1ll1_opy_.get_logger(self.__class__.__name__, bstack11111l1ll1_opy_.bstack1l1l1ll111l_opy_())
        self.bstack1l1l11ll1ll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll111llll_opy_ = bstack1lll11l111l_opy_()
        self.bstack1l1l11l1l11_opy_ = None
        self.bstack1ll1ll11l11_opy_ = None
        self.bstack1l1l1ll1111_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l1l1l111_opy_ = []
    def bstack1ll1llll1l_opy_(self):
        return os.environ.get(bstack1l1ll11l11_opy_).lower().__eq__(bstack11ll1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣጮ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l11lllll1l_opy_, bstack11ll1ll_opy_ (u"ࠫࠬጯ")).lower() in [bstack11ll1ll_opy_ (u"ࠬࡺࡲࡶࡧࠪጰ"), bstack11ll1ll_opy_ (u"࠭࠱ࠨጱ"), bstack11ll1ll_opy_ (u"ࠧࡺࡧࡶࠫጲ")]:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡈࡲࡶࡨ࡯࡮ࡨࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡲࡵࡤࡦࠢࡧࡹࡪࠦࡴࡰࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡒࡖࡈࡋ࡟ࡇࡃࡏࡐࡇࡇࡃࡌࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺࠠࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠤጳ"))
            os.environ[bstack11ll1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡋࡖࡣࡗ࡛ࡎࡏࡋࡑࡋࠧጴ")] = bstack11ll1ll_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤጵ")
            return False
        if bstack11ll1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨጶ") in config and str(config[bstack11ll1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩጷ")]).lower() != bstack11ll1ll_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬጸ"):
            return False
        bstack1l1l11ll11l_opy_ = [bstack11ll1ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢጹ"), bstack11ll1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧጺ")]
        bstack1l11ll11l1l_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧጻ")) in bstack1l1l11ll11l_opy_ or os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫጼ")) in bstack1l1l11ll11l_opy_
        os.environ[bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡍࡘࡥࡒࡖࡐࡑࡍࡓࡍࠢጽ")] = str(bstack1l11ll11l1l_opy_) # bstack1l1l111ll1l_opy_ bstack1l11llll1ll_opy_ VAR to bstack1l11lll111l_opy_ is binary running
        return bstack1l11ll11l1l_opy_
    def bstack1lll1l1l11_opy_(self):
        for event in bstack1l1l1llll1l_opy_:
            bstack1l1llll11l_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l1llll11l_opy_.logger.debug(bstack11ll1ll_opy_ (u"ࠧࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠤࡂࡄࠠࡼࡣࡵ࡫ࡸࢃࠠࠣጾ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠨࠢጿ"))
            )
        bstack1l1llll11l_opy_.register(Events.bstack111l1111ll_opy_, self.__1l1l1lllll1_opy_)
        bstack1l1llll11l_opy_.register(Events.CONNECT, self.__1l1l1ll1ll1_opy_)
        bstack1l1llll11l_opy_.register(Events.bstack11lll1ll1l_opy_, self.__1l1l11l1111_opy_)
        bstack1l1llll11l_opy_.register(Events.bstack1ll11l1l1_opy_, self.__1l1l1111lll_opy_)
    def bstack1lllll1l1l_opy_(self):
        return not self.bstack1l11ll111ll_opy_ and os.environ.get(bstack1l1l1ll1l11_opy_, bstack11ll1ll_opy_ (u"ࠢࠣፀ")) != bstack11ll1ll_opy_ (u"ࠣࠤፁ")
    def is_running(self):
        if self.bstack1l11ll111ll_opy_:
            return self.bstack1l1l11l111l_opy_
        else:
            return bool(self.bstack1l11ll11lll_opy_)
    def bstack1l11ll111l1_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l1l1l111_opy_) and cli.is_running()
    def __1l1l1lll1ll_opy_(self, bstack1l1l11lll11_opy_=10):
        if self.bstack1llllll1l1l_opy_:
            return
        bstack111111ll11_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l1ll1lll_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠤ࡞ࠦፂ") + str(id(self)) + bstack11ll1ll_opy_ (u"ࠥࡡࠥࡩ࡯࡯ࡰࡨࡧࡹ࡯࡮ࡨࠤፃ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11ll1ll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠰ࡨࡲࡦࡨ࡬ࡦࡡ࡫ࡸࡹࡶ࡟ࡱࡴࡲࡼࡾࠨፄ"), 0), (bstack11ll1ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠱ࡩࡳࡧࡢ࡭ࡧࡢ࡬ࡹࡺࡰࡴࡡࡳࡶࡴࡾࡹࠣፅ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l11lll11_opy_)
        self.bstack1l11ll11lll_opy_ = channel
        self.bstack1llllll1l1l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l11ll11lll_opy_)
        self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡨࡵ࡮࡯ࡧࡦࡸࠧፆ"), datetime.now() - bstack111111ll11_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l1ll1lll_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥ࠼ࠣ࡭ࡸࡥࡣࡩ࡫࡯ࡨࡤࡶࡲࡰࡥࡨࡷࡸࡃࠢፇ") + str(self.bstack1lllll1l1l_opy_()) + bstack11ll1ll_opy_ (u"ࠣࠤፈ"))
    def __1l1l11l1111_opy_(self, event_name):
        if self.bstack1lllll1l1l_opy_():
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡷࡹࡵࡰࡱ࡫ࡱ࡫ࠥࡉࡌࡊࠤፉ"))
        self.__1l11lll1l11_opy_()
    def __1l1l1111lll_opy_(self, event_name, bstack1l1l1lll1l1_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠥࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠥፊ"))
        bstack1l11ll1l111_opy_ = Path(bstack1lll1ll1l11_opy_ (u"ࠦࢀࡹࡥ࡭ࡨ࠱ࡧࡱ࡯࡟ࡥ࡫ࡵࢁ࠴ࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࡹ࠮࡫ࡵࡲࡲࠧፋ"))
        if self.bstack1l1l1llllll_opy_ and bstack1l11ll1l111_opy_.exists():
            with open(bstack1l11ll1l111_opy_, bstack11ll1ll_opy_ (u"ࠬࡸࠧፌ"), encoding=bstack11ll1ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬፍ")) as fp:
                data = json.load(fp)
                try:
                    bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠧࡑࡑࡖࡘࠬፎ"), bstack11l1l1l1l1_opy_(bstack1l11ll1ll1_opy_), data, {
                        bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸ࡭࠭ፏ"): (self.config[bstack11ll1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫፐ")], self.config[bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ፑ")])
                    })
                except Exception as e:
                    logger.debug(bstack1l1l1ll1l_opy_.format(str(e)))
            bstack1l11ll1l111_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l111111l_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1l1l1lllll1_opy_(self, event_name: str, data):
        from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
        self.bstack1l11ll1llll_opy_, self.bstack1l1l1llllll_opy_ = bstack1l11llll111_opy_(data.bs_config)
        os.environ[bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡛ࡗࡏࡔࡂࡄࡏࡉࡤࡊࡉࡓࠩፒ")] = self.bstack1l1l1llllll_opy_
        if not self.bstack1l11ll1llll_opy_ or not self.bstack1l1l1llllll_opy_:
            raise ValueError(bstack11ll1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡴࡩࡧࠣࡗࡉࡑࠠࡄࡎࡌࠤࡧ࡯࡮ࡢࡴࡼࠦፓ"))
        if self.bstack1lllll1l1l_opy_():
            self.__1l1l1ll1ll1_opy_(event_name, bstack1l1ll11ll_opy_())
            return
        try:
            bstack1llll11l11l_opy_.end(EVENTS.bstack11l1lll111_opy_.value, EVENTS.bstack11l1lll111_opy_.value + bstack11ll1ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨፔ"), EVENTS.bstack11l1lll111_opy_.value + bstack11ll1ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧፕ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11ll1ll_opy_ (u"ࠣࡅࡲࡱࡵࡲࡥࡵࡧࠣࡗࡉࡑࠠࡔࡧࡷࡹࡵ࠴ࠢፖ"))
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵࠣࡿࢂࠨፗ").format(e))
        start = datetime.now()
        is_started = self.__1l11ll1l1l1_opy_()
        self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥࡷࡵࡧࡷ࡯ࡡࡷ࡭ࡲ࡫ࠢፘ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l1lll1ll_opy_()
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥፙ"), datetime.now() - start)
            start = datetime.now()
            self.__1l11ll1l11l_opy_(data)
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥፚ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l11lll11l1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1l1l1ll1ll1_opy_(self, event_name: str, data: bstack1l1ll11ll_opy_):
        if not self.bstack1lllll1l1l_opy_():
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦࡳࡳࡴࡥࡤࡶ࠽ࠤࡳࡵࡴࠡࡣࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࠥ፛"))
            return
        bin_session_id = os.environ.get(bstack1l1l1ll1l11_opy_)
        start = datetime.now()
        self.__1l1l1lll1ll_opy_()
        self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨ፜"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠤࡹࡵࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢࡆࡐࡎࠦࠢ፝") + str(bin_session_id) + bstack11ll1ll_opy_ (u"ࠤࠥ፞"))
        start = datetime.now()
        self.__1l1l1ll11l1_opy_()
        self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣ፟"), datetime.now() - start)
    def __1l11ll11111_opy_(self):
        if not self.bstack1llllll1l1l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡨࡧ࡮࡯ࡱࡷࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࠠ࡮ࡱࡧࡹࡱ࡫ࡳࠣ፠"))
            return
        bstack1l11ll1l1ll_opy_ = {
            bstack11ll1ll_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ፡"): (bstack1ll1ll1l111_opy_, bstack1lll11l11ll_opy_, bstack1lll11l1l11_opy_),
            bstack11ll1ll_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ።"): (bstack1llll11l1ll_opy_, bstack1lll11111l1_opy_, bstack1llll1ll111_opy_),
        }
        if not self.bstack1l1l11l1l11_opy_ and self.session_framework in bstack1l11ll1l1ll_opy_:
            bstack1l1l11ll111_opy_, bstack1l11lllll11_opy_, bstack1l1l11lll1l_opy_ = bstack1l11ll1l1ll_opy_[self.session_framework]
            bstack1l1l1llll11_opy_ = bstack1l11lllll11_opy_()
            self.bstack1ll1ll11l11_opy_ = bstack1l1l1llll11_opy_
            self.bstack1l1l11l1l11_opy_ = bstack1l1l11lll1l_opy_
            self.bstack1l1l1l1l111_opy_.append(bstack1l1l1llll11_opy_)
            self.bstack1l1l1l1l111_opy_.append(bstack1l1l11ll111_opy_(self.bstack1ll1ll11l11_opy_))
        if not self.bstack1l1l1ll1111_opy_ and self.config_observability and self.config_observability.success: # bstack1llll111ll1_opy_
            self.bstack1l1l1ll1111_opy_ = bstack1l1l1l1l1l1_opy_(self.bstack1l1l11l1l11_opy_, self.bstack1ll1ll11l11_opy_) # bstack1l1l111ll11_opy_
            self.bstack1l1l1l1l111_opy_.append(self.bstack1l1l1ll1111_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l11l1lll_opy_(self.bstack1l1l11l1l11_opy_, self.bstack1ll1ll11l11_opy_)
            self.bstack1l1l1l1l111_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11ll1ll_opy_ (u"ࠢࡴࡧ࡯ࡪࡍ࡫ࡡ࡭ࠤ፣"), False) == True:
            self.ai = bstack1l1ll111l1l_opy_()
            self.bstack1l1l1l1l111_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l1l1ll1l_opy_ and self.bstack1l1l1l1ll1l_opy_.success:
            self.percy = bstack1l11lll11ll_opy_(self.bstack1l1l1l1ll1l_opy_)
            self.bstack1l1l1l1l111_opy_.append(self.percy)
        for mod in self.bstack1l1l1l1l111_opy_:
            if not mod.bstack1lll11l1111_opy_():
                mod.configure(self.bstack1llllll1l1l_opy_, self.config, self.cli_bin_session_id, self.bstack1lll111llll_opy_)
    def __1l11lllllll_opy_(self):
        for mod in self.bstack1l1l1l1l111_opy_:
            if mod.bstack1lll11l1111_opy_():
                mod.configure(self.bstack1llllll1l1l_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l1l11111ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1l11ll1l11l_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l1l1ll11_opy_:
            return
        self.__1l1l11llll1_opy_(data)
        bstack111111ll11_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11ll1ll_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣ፤")
        req.sdk_language = bstack11ll1ll_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤ፥")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l111lll1_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥ࡟ࠧ፦") + str(id(self)) + bstack11ll1ll_opy_ (u"ࠦࡢࠦ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡳࡵࡣࡵࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥ፧"))
            r = self.bstack1llllll1l1l_opy_.StartBinSession(req)
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡹࡧࡲࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢ፨"), datetime.now() - bstack111111ll11_opy_)
            os.environ[bstack1l1l1ll1l11_opy_] = r.bin_session_id
            self.__1l1l1l11ll1_opy_(r)
            self.__1l11ll11111_opy_()
            self.bstack1lll111llll_opy_.start()
            self.bstack1l1l1l1ll11_opy_ = True
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡛ࠣ፩") + str(id(self)) + bstack11ll1ll_opy_ (u"ࠢ࡞ࠢࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠧ፪"))
        except grpc.bstack1l1l111l1ll_opy_ as bstack1l1l1l111l1_opy_:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡵ࡫ࡰࡩࡴ࡫ࡵࡵ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥ፫") + str(bstack1l1l1l111l1_opy_) + bstack11ll1ll_opy_ (u"ࠤࠥ፬"))
            traceback.print_exc()
            raise bstack1l1l1l111l1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢ፭") + str(e) + bstack11ll1ll_opy_ (u"ࠦࠧ፮"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l1l1lll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1l1l1ll11l1_opy_(self):
        if not self.bstack1lllll1l1l_opy_() or not self.cli_bin_session_id or self.bstack1l1l11ll1l1_opy_:
            return
        bstack111111ll11_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ፯"), bstack11ll1ll_opy_ (u"࠭࠰ࠨ፰")))
        try:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢ࡜ࠤ፱") + str(id(self)) + bstack11ll1ll_opy_ (u"ࠣ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥ፲"))
            r = self.bstack1llllll1l1l_opy_.ConnectBinSession(req)
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡤࡱࡱࡲࡪࡩࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨ፳"), datetime.now() - bstack111111ll11_opy_)
            self.__1l1l1l11ll1_opy_(r)
            self.__1l11ll11111_opy_()
            self.bstack1lll111llll_opy_.start()
            self.bstack1l1l11ll1l1_opy_ = True
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥ࡟ࠧ፴") + str(id(self)) + bstack11ll1ll_opy_ (u"ࠦࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦࠥ፵"))
        except grpc.bstack1l1l111l1ll_opy_ as bstack1l1l1l111l1_opy_:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡹ࡯࡭ࡦࡱࡨࡹࡹ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢ፶") + str(bstack1l1l1l111l1_opy_) + bstack11ll1ll_opy_ (u"ࠨࠢ፷"))
            traceback.print_exc()
            raise bstack1l1l1l111l1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦ፸") + str(e) + bstack11ll1ll_opy_ (u"ࠣࠤ፹"))
            traceback.print_exc()
            raise e
    def __1l1l1l11ll1_opy_(self, r):
        self.bstack1l1l1ll1l1l_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11ll1ll_opy_ (u"ࠤࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡳࡦࡴࡹࡩࡷࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣ፺") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11ll1ll_opy_ (u"ࠥࡩࡲࡶࡴࡺࠢࡦࡳࡳ࡬ࡩࡨࠢࡩࡳࡺࡴࡤࠣ፻"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11ll1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡨࡶࡨࡿࠠࡪࡵࠣࡷࡪࡴࡴࠡࡱࡱࡰࡾࠦࡡࡴࠢࡳࡥࡷࡺࠠࡰࡨࠣࡸ࡭࡫ࠠࠣࡅࡲࡲࡳ࡫ࡣࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲ࠱ࠨࠠࡢࡰࡧࠤࡹ࡮ࡩࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤ࡮ࡹࠠࡢ࡮ࡶࡳࠥࡻࡳࡦࡦࠣࡦࡾࠦࡓࡵࡣࡵࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࡲࡦࡨࡲࡶࡪ࠲ࠠࡏࡱࡱࡩࠥ࡮ࡡ࡯ࡦ࡯࡭ࡳ࡭ࠠࡪࡵࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ፼")
        self.bstack1l1l1l1ll1l_opy_ = getattr(r, bstack11ll1ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ፽"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ፾")] = self.config_testhub.jwt
        os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ፿")] = self.config_testhub.build_hashed_id
    def bstack1l11lll1ll1_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1l11l111l_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1l1111ll1_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1l1111ll1_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l11lll1ll1_opy_(event_name=EVENTS.bstack1l1l1ll11ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1l11ll1l1l1_opy_(self, bstack1l1l11lll11_opy_=10):
        if self.bstack1l1l11l111l_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡵࡷࡥࡷࡺ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡵࡹࡳࡴࡩ࡯ࡩࠥᎀ"))
            return True
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡶࡸࡦࡸࡴࠣᎁ"))
        if os.getenv(bstack11ll1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡅࡏࡘࠥᎂ")) == bstack1l1l1111l1l_opy_:
            self.cli_bin_session_id = bstack1l1l1111l1l_opy_
            self.cli_listen_addr = bstack11ll1ll_opy_ (u"ࠦࡺࡴࡩࡹ࠼࠲ࡸࡲࡶ࠯ࡴࡦ࡮࠱ࡵࡲࡡࡵࡨࡲࡶࡲ࠳ࠥࡴ࠰ࡶࡳࡨࡱࠢᎃ") % (self.cli_bin_session_id)
            self.bstack1l1l11l111l_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l11ll1llll_opy_, bstack11ll1ll_opy_ (u"ࠧࡹࡤ࡬ࠤᎄ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1111111_opy_ compat for text=True in bstack1l1l1l1111l_opy_ python
            encoding=bstack11ll1ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᎅ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1l1l11l1l_opy_ = threading.Thread(target=self.__1l1l11l11l1_opy_, args=(bstack1l1l11lll11_opy_,))
        bstack1l1l1l11l1l_opy_.start()
        bstack1l1l1l11l1l_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡳࡱࡣࡺࡲ࠿ࠦࡲࡦࡶࡸࡶࡳࡩ࡯ࡥࡧࡀࡿࡸ࡫࡬ࡧ࠰ࡳࡶࡴࡩࡥࡴࡵ࠱ࡶࡪࡺࡵࡳࡰࡦࡳࡩ࡫ࡽࠡࡱࡸࡸࡂࢁࡳࡦ࡮ࡩ࠲ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡹࡴࡥࡱࡸࡸ࠳ࡸࡥࡢࡦࠫ࠭ࢂࠦࡥࡳࡴࡀࠦᎆ") + str(self.process.stderr.read()) + bstack11ll1ll_opy_ (u"ࠣࠤᎇ"))
        if not self.bstack1l1l11l111l_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤ࡞ࠦᎈ") + str(id(self)) + bstack11ll1ll_opy_ (u"ࠥࡡࠥࡩ࡬ࡦࡣࡱࡹࡵࠨᎉ"))
            self.__1l11lll1l11_opy_()
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡴࡷࡵࡣࡦࡵࡶࡣࡷ࡫ࡡࡥࡻ࠽ࠤࠧᎊ") + str(self.bstack1l1l11l111l_opy_) + bstack11ll1ll_opy_ (u"ࠧࠨᎋ"))
        return self.bstack1l1l11l111l_opy_
    def __1l1l11l11l1_opy_(self, bstack1l1l11111l1_opy_=10):
        bstack1l11ll1ll11_opy_ = time.time()
        while self.process and time.time() - bstack1l11ll1ll11_opy_ < bstack1l1l11111l1_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11ll1ll_opy_ (u"ࠨࡩࡥ࠿ࠥᎌ") in line:
                    self.cli_bin_session_id = line.split(bstack11ll1ll_opy_ (u"ࠢࡪࡦࡀࠦᎍ"))[-1:][0].strip()
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡥ࡯࡭ࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡀࠢᎎ") + str(self.cli_bin_session_id) + bstack11ll1ll_opy_ (u"ࠤࠥᎏ"))
                    continue
                if bstack11ll1ll_opy_ (u"ࠥࡰ࡮ࡹࡴࡦࡰࡀࠦ᎐") in line:
                    self.cli_listen_addr = line.split(bstack11ll1ll_opy_ (u"ࠦࡱ࡯ࡳࡵࡧࡱࡁࠧ᎑"))[-1:][0].strip()
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡩ࡬ࡪࡡ࡯࡭ࡸࡺࡥ࡯ࡡࡤࡨࡩࡸ࠺ࠣ᎒") + str(self.cli_listen_addr) + bstack11ll1ll_opy_ (u"ࠨࠢ᎓"))
                    continue
                if bstack11ll1ll_opy_ (u"ࠢࡱࡱࡵࡸࡂࠨ᎔") in line:
                    port = line.split(bstack11ll1ll_opy_ (u"ࠣࡲࡲࡶࡹࡃࠢ᎕"))[-1:][0].strip()
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡳࡳࡷࡺ࠺ࠣ᎖") + str(port) + bstack11ll1ll_opy_ (u"ࠥࠦ᎗"))
                    continue
                if line.strip() == bstack1l11llll1l1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11ll1ll_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡍࡔࡥࡓࡕࡔࡈࡅࡒࠨ᎘"), bstack11ll1ll_opy_ (u"ࠧ࠷ࠢ᎙")) == bstack11ll1ll_opy_ (u"ࠨ࠱ࠣ᎚"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1l11l111l_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࡀࠠࠣ᎛") + str(e) + bstack11ll1ll_opy_ (u"ࠣࠤ᎜"))
        return False
    @measure(event_name=EVENTS.bstack1l1l11l1l1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1l11lll1l11_opy_(self):
        if self.bstack1l11ll11lll_opy_:
            self.bstack1lll111llll_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l1l1l11l_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l11ll1l1_opy_:
                    self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠤࡶࡸࡴࡶ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨ᎝"), datetime.now() - start)
                else:
                    self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥࡷࡹࡵࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢ᎞"), datetime.now() - start)
            self.__1l11lllllll_opy_()
            start = datetime.now()
            self.bstack1l11ll11lll_opy_.close()
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠦࡩ࡯ࡳࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨ᎟"), datetime.now() - start)
            self.bstack1l11ll11lll_opy_ = None
        if self.process:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡹࡴࡰࡲࠥᎠ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠨ࡫ࡪ࡮࡯ࡣࡹ࡯࡭ࡦࠤᎡ"), datetime.now() - start)
            self.process = None
            if self.bstack1l11ll111ll_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack11l1lll11_opy_()
                self.logger.info(
                    bstack11ll1ll_opy_ (u"ࠢࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠢᎢ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᎣ")] = self.config_testhub.build_hashed_id
        self.bstack1l1l11l111l_opy_ = False
    def __1l1l11llll1_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11ll1ll_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᎤ")] = selenium.__version__
            data.frameworks.append(bstack11ll1ll_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᎥ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack11ll1ll_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᎦ")] = __version__
            data.frameworks.append(bstack11ll1ll_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᎧ"))
        except:
            pass
    def bstack1l11llll11l_opy_(self, hub_url: str, platform_index: int, bstack1ll1ll1ll1_opy_: Any):
        if self.bstack1llll1lll1l_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠠࡴࡧࡷࡹࡵࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡷࡪࡺࠠࡶࡲࠥᎨ"))
            return
        try:
            bstack111111ll11_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11ll1ll_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᎩ")
            self.bstack1llll1lll1l_opy_ = bstack1llll1ll111_opy_(
                cli.config.get(bstack11ll1ll_opy_ (u"ࠣࡪࡸࡦ࡚ࡸ࡬ࠣᎪ"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll1ll1ll_opy_={bstack11ll1ll_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨᎫ"): bstack1ll1ll1ll1_opy_}
            )
            def bstack1l11l1lllll_opy_(self):
                return
            if self.config.get(bstack11ll1ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠧᎬ"), True):
                Service.start = bstack1l11l1lllll_opy_
                Service.stop = bstack1l11l1lllll_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack1lll1l1ll1_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11llll11_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᎭ"), datetime.now() - bstack111111ll11_opy_)
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠼ࠣࠦᎮ") + str(e) + bstack11ll1ll_opy_ (u"ࠨࠢᎯ"))
    def bstack1l1l1l11l11_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1l1ll1llll_opy_
            self.bstack1llll1lll1l_opy_ = bstack1lll11l1l11_opy_(
                platform_index,
                framework_name=bstack11ll1ll_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᎰ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠺ࠡࠤᎱ") + str(e) + bstack11ll1ll_opy_ (u"ࠤࠥᎲ"))
            pass
    def bstack1l1l111llll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠤࡸ࡫ࡴࡶࡲࠣࡴࡾࡺࡥࡴࡶ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡹࡥࡵࠢࡸࡴࠧᎳ"))
            return
        if bstack1llllll1l1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᎴ"): pytest.__version__ }, [bstack11ll1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᎵ")], self.bstack1lll111llll_opy_, self.bstack1llllll1l1l_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l11lll1lll_opy_({ bstack11ll1ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᎶ"): pytest.__version__ }, [bstack11ll1ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᎷ")], self.bstack1lll111llll_opy_, self.bstack1llllll1l1l_opy_)
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡾࡺࡥࡴࡶ࠽ࠤࠧᎸ") + str(e) + bstack11ll1ll_opy_ (u"ࠤࠥᎹ"))
        self.bstack1l11lll1111_opy_()
    def bstack1l11lll1111_opy_(self):
        if not self.bstack1ll1llll1l_opy_():
            return
        bstack111lll11l1_opy_ = None
        def bstack111ll11l11_opy_(config, startdir):
            return bstack11ll1ll_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀ࠶ࡽࠣᎺ").format(bstack11ll1ll_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥᎻ"))
        def bstack11l11l1ll_opy_():
            return
        def bstack1l1llll11_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11ll1ll_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬᎼ"):
                return bstack11ll1ll_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧᎽ")
            else:
                return bstack111lll11l1_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack111lll11l1_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack111ll11l11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11l11l1ll_opy_
            Config.getoption = bstack1l1llll11_opy_
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡺࡣࡩࠢࡳࡽࡹ࡫ࡳࡵࠢࡶࡩࡱ࡫࡮ࡪࡷࡰࠤ࡫ࡵࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠺ࠡࠤᎾ") + str(e) + bstack11ll1ll_opy_ (u"ࠣࠤᎿ"))
    def bstack1l1l1l111ll_opy_(self):
        bstack1111l11111_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1111l11111_opy_, dict):
            if cli.config_observability:
                bstack1111l11111_opy_.update(
                    {bstack11ll1ll_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤᏀ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11ll1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࡤࡺ࡯ࡠࡹࡵࡥࡵࠨᏁ") in accessibility.get(bstack11ll1ll_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᏂ"), {}):
                    bstack1l1l11l1ll1_opy_ = accessibility.get(bstack11ll1ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᏃ"))
                    bstack1l1l11l1ll1_opy_.update({ bstack11ll1ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡕࡱ࡚ࡶࡦࡶࠢᏄ"): bstack1l1l11l1ll1_opy_.pop(bstack11ll1ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡡࡷࡳࡤࡽࡲࡢࡲࠥᏅ")) })
                bstack1111l11111_opy_.update({bstack11ll1ll_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᏆ"): accessibility })
        return bstack1111l11111_opy_
    @measure(event_name=EVENTS.bstack1l1l1111l11_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1l1l1l1l11l_opy_(self, bstack1l11ll11ll1_opy_: str = None, bstack1l1l111l111_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1llllll1l1l_opy_:
            return
        bstack111111ll11_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l11ll11ll1_opy_:
            req.bstack1l11ll11ll1_opy_ = bstack1l11ll11ll1_opy_
        if bstack1l1l111l111_opy_:
            req.bstack1l1l111l111_opy_ = bstack1l1l111l111_opy_
        try:
            r = self.bstack1llllll1l1l_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡶࡲࡴࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥᏇ"), datetime.now() - bstack111111ll11_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack11lllll111_opy_(self, key: str, value: timedelta):
        tag = bstack11ll1ll_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࠥᏈ") if self.bstack1lllll1l1l_opy_() else bstack11ll1ll_opy_ (u"ࠦࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵࠥᏉ")
        self.bstack1l1l11ll1ll_opy_[bstack11ll1ll_opy_ (u"ࠧࡀࠢᏊ").join([tag + bstack11ll1ll_opy_ (u"ࠨ࠭ࠣᏋ") + str(id(self)), key])] += value
    def bstack11l1lll11_opy_(self):
        if not os.getenv(bstack11ll1ll_opy_ (u"ࠢࡅࡇࡅ࡙ࡌࡥࡐࡆࡔࡉࠦᏌ"), bstack11ll1ll_opy_ (u"ࠣ࠲ࠥᏍ")) == bstack11ll1ll_opy_ (u"ࠤ࠴ࠦᏎ"):
            return
        bstack1l11ll1lll1_opy_ = dict()
        bstack1llll111111_opy_ = []
        if self.test_framework:
            bstack1llll111111_opy_.extend(list(self.test_framework.bstack1llll111111_opy_.values()))
        if self.bstack1llll1lll1l_opy_:
            bstack1llll111111_opy_.extend(list(self.bstack1llll1lll1l_opy_.bstack1llll111111_opy_.values()))
        for instance in bstack1llll111111_opy_:
            if not instance.platform_index in bstack1l11ll1lll1_opy_:
                bstack1l11ll1lll1_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l11ll1lll1_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll1111l_opy_().items():
                report[k] += v
                report[k.split(bstack11ll1ll_opy_ (u"ࠥ࠾ࠧᏏ"))[0]] += v
        bstack1l1l1l1llll_opy_ = sorted([(k, v) for k, v in self.bstack1l1l11ll1ll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l11llllll1_opy_ = 0
        for r in bstack1l1l1l1llll_opy_:
            bstack1l1l11lllll_opy_ = r[1].total_seconds()
            bstack1l11llllll1_opy_ += bstack1l1l11lllll_opy_
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻ࡽࡵ࡟࠵ࡣࡽ࠾ࠤᏐ") + str(bstack1l1l11lllll_opy_) + bstack11ll1ll_opy_ (u"ࠧࠨᏑ"))
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࠭࠮ࠤᏒ"))
        bstack1l1l11l11ll_opy_ = []
        for platform_index, report in bstack1l11ll1lll1_opy_.items():
            bstack1l1l11l11ll_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l11l11ll_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1ll1lllll_opy_ = set()
        bstack1l1l1l1l1ll_opy_ = 0
        for r in bstack1l1l11l11ll_opy_:
            bstack1l1l11lllll_opy_ = r[2].total_seconds()
            bstack1l1l1l1l1ll_opy_ += bstack1l1l11lllll_opy_
            bstack1ll1lllll_opy_.add(r[0])
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡵࡧࡶࡸ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࡼࡴ࡞࠴ࡢࢃ࠺ࡼࡴ࡞࠵ࡢࢃ࠽ࠣᏓ") + str(bstack1l1l11lllll_opy_) + bstack11ll1ll_opy_ (u"ࠣࠤᏔ"))
        if self.bstack1lllll1l1l_opy_():
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤ࠰࠱ࠧᏕ"))
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡧࡱ࡯࠺ࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠽ࡼࡶࡲࡸࡦࡲ࡟ࡤ࡮࡬ࢁࠥࡺࡥࡴࡶ࠽ࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠳ࡻࡴࡶࡵࠬࡵࡲࡡࡵࡨࡲࡶࡲࡹࠩࡾ࠿ࠥᏖ") + str(bstack1l1l1l1l1ll_opy_) + bstack11ll1ll_opy_ (u"ࠦࠧᏗ"))
        else:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠾ࠤᏘ") + str(bstack1l11llllll1_opy_) + bstack11ll1ll_opy_ (u"ࠨࠢᏙ"))
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠢ࠮࠯ࠥᏚ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1llllll1l1l_opy_:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡥ࡯࡭ࡤࡹࡥࡳࡸ࡬ࡧࡪࠦࡩࡴࠢࡱࡳࡹࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࡧ࠲ࠥࡉࡡ࡯ࡰࡲࡸࠥࡶࡥࡳࡨࡲࡶࡲࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧᏛ"))
            return None
        response = self.bstack1llllll1l1l_opy_.TestOrchestration(request)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࠭ࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠭ࡴࡧࡶࡷ࡮ࡵ࡮࠾ࡽࢀࠦᏜ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l1ll1l1l_opy_(self, r):
        if r is not None and getattr(r, bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࠫᏝ"), None) and getattr(r.testhub, bstack11ll1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫᏞ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11ll1ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᏟ")))
            for bstack1l1l111l11l_opy_, err in errors.items():
                if err[bstack11ll1ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᏠ")] == bstack11ll1ll_opy_ (u"ࠧࡪࡰࡩࡳࠬᏡ"):
                    self.logger.info(err[bstack11ll1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᏢ")])
                else:
                    self.logger.error(err[bstack11ll1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᏣ")])
    def bstack1l1ll1l11l_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()