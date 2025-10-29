# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1l1_opy_ import bstack1l11ll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll11111l_opy_ import bstack1l1ll11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l11ll111_opy_ import bstack1l11llll111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l1l_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111l1l_opy_ import bstack1lll111l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll1l11l_opy_ import bstack1ll1ll11l11_opy_
from browserstack_sdk.sdk_cli.bstack1llll111l11_opy_ import bstack1lll1lll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1l11lllll1l_opy_ import bstack1l1l1ll1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1lll_opy_ import bstack1lll1l1lll_opy_, Events, bstack1l1111ll1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1ll1lll_opy_ import bstack1l11lll1111_opy_
from browserstack_sdk.sdk_cli.bstack1llll11llll_opy_ import bstack1llll1l111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1ll1llllll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1lll1_opy_ import bstack1lll1l111l1_opy_
from bstack_utils.helper import Notset, bstack1l1l1ll1ll1_opy_, get_cli_dir, bstack1l1l11ll11l_opy_, bstack11ll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1l1lllll11l_opy_ import bstack1ll11l1llll_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11ll1ll_opy_ import bstack11lll1l1l_opy_
from bstack_utils.helper import Notset, bstack1l1l1ll1ll1_opy_, get_cli_dir, bstack1l1l11ll11l_opy_, bstack11ll1l1l1_opy_, bstack1l111lll1_opy_, bstack11l111111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11l1_opy_, bstack1lll1l1l11l_opy_, bstack1lll1l1llll_opy_, bstack1ll1l1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll1llll1_opy_, bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_
from bstack_utils.constants import *
from bstack_utils.bstack11l1ll111_opy_ import bstack1l11lll1l1_opy_
from bstack_utils import bstack11l1l11ll1_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111llll111_opy_, bstack111ll111l_opy_
logger = bstack11l1l11ll1_opy_.get_logger(__name__, bstack11l1l11ll1_opy_.bstack1l1l11llll1_opy_())
def bstack1l1l1llll1l_opy_(bs_config):
    bstack1l1l1111l1l_opy_ = None
    bstack1l1l11111ll_opy_ = None
    try:
        bstack1l1l11111ll_opy_ = get_cli_dir()
        bstack1l1l1111l1l_opy_ = bstack1l1l11ll11l_opy_(bstack1l1l11111ll_opy_)
        bstack1l1l111l11l_opy_ = bstack1l1l1ll1ll1_opy_(bstack1l1l1111l1l_opy_, bstack1l1l11111ll_opy_, bs_config)
        bstack1l1l1111l1l_opy_ = bstack1l1l111l11l_opy_ if bstack1l1l111l11l_opy_ else bstack1l1l1111l1l_opy_
        if not bstack1l1l1111l1l_opy_:
            raise ValueError(bstack11l11ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠨጘ"))
    except Exception as ex:
        logger.debug(bstack11l11ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡰࡦࡺࡥࡴࡶࠣࡦ࡮ࡴࡡࡳࡻࠣࡿࢂࠨጙ").format(ex))
        bstack1l1l1111l1l_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠢጚ"))
        if bstack1l1l1111l1l_opy_:
            logger.debug(bstack11l11ll_opy_ (u"ࠧࡌࡡ࡭࡮࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࠤࡹࡵࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠣࡪࡷࡵ࡭ࠡࡧࡱࡺ࡮ࡸ࡯࡯࡯ࡨࡲࡹࡀࠠࠣጛ") + str(bstack1l1l1111l1l_opy_) + bstack11l11ll_opy_ (u"ࠨࠢጜ"))
        else:
            logger.debug(bstack11l11ll_opy_ (u"ࠢࡏࡱࠣࡺࡦࡲࡩࡥࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸࡀࠦࡳࡦࡶࡸࡴࠥࡳࡡࡺࠢࡥࡩࠥ࡯࡮ࡤࡱࡰࡴࡱ࡫ࡴࡦ࠰ࠥጝ"))
    return bstack1l1l1111l1l_opy_, bstack1l1l11111ll_opy_
bstack1l1l1l11l1l_opy_ = bstack11l11ll_opy_ (u"ࠣ࠻࠼࠽࠾ࠨጞ")
bstack1l1l1l1lll1_opy_ = bstack11l11ll_opy_ (u"ࠤࡵࡩࡦࡪࡹࠣጟ")
bstack1l1l11l1l11_opy_ = bstack11l11ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢጠ")
bstack1l1l11111l1_opy_ = bstack11l11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡑࡏࡓࡕࡇࡑࡣࡆࡊࡄࡓࠤጡ")
bstack11l11l11l1_opy_ = bstack11l11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣጢ")
bstack1l1l111l111_opy_ = re.compile(bstack11l11ll_opy_ (u"ࡸࠢࠩࡁ࡬࠭࠳࠰ࠨࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࢂࡂࡔࠫ࠱࠮ࠧጣ"))
bstack1l11lllll11_opy_ = bstack11l11ll_opy_ (u"ࠢࡥࡧࡹࡩࡱࡵࡰ࡮ࡧࡱࡸࠧጤ")
bstack1l1l11l11l1_opy_ = bstack11l11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡑࡕࡇࡊࡥࡆࡂࡎࡏࡆࡆࡉࡋࠣጥ")
bstack1l1l1lll111_opy_ = [
    Events.bstack111lll11l_opy_,
    Events.CONNECT,
    Events.bstack1l111l1111_opy_,
]
class SDKCLI:
    _1ll1l1ll1ll_opy_ = None
    process: Union[None, Any]
    bstack1l1l11l1lll_opy_: bool
    bstack1l1l1l11lll_opy_: bool
    bstack1l1l1l1l111_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1l11lll1l_opy_: Union[None, grpc.Channel]
    bstack1l1l11l1ll1_opy_: str
    test_framework: TestFramework
    bstack1lllll1l11l_opy_: bstack1ll1llllll1_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l11llllll1_opy_: bstack1l1l1ll1l1l_opy_
    accessibility: bstack1l11ll111l1_opy_
    bstack1ll11ll1ll_opy_: bstack11lll1l1l_opy_
    ai: bstack1l1ll11l1ll_opy_
    bstack1l11ll11lll_opy_: bstack1l11llll111_opy_
    bstack1l11ll1111l_opy_: List[bstack1lllll11111_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l11lll1l1l_opy_: Any
    bstack1l1l111lll1_opy_: Dict[str, timedelta]
    bstack1l1l111l1l1_opy_: str
    bstack1lll11l11l1_opy_: bstack1lll11l1111_opy_
    def __new__(cls):
        if not cls._1ll1l1ll1ll_opy_:
            cls._1ll1l1ll1ll_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1l1ll1ll_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1l11l1lll_opy_ = False
        self.bstack1l1l11lll1l_opy_ = None
        self.bstack1llll1l1ll1_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l11111l1_opy_, None)
        self.bstack1l11lll1l11_opy_ = os.environ.get(bstack1l1l11l1l11_opy_, bstack11l11ll_opy_ (u"ࠤࠥጦ")) == bstack11l11ll_opy_ (u"ࠥࠦጧ")
        self.bstack1l1l1l11lll_opy_ = False
        self.bstack1l1l1l1l111_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l11lll1l1l_opy_ = None
        self.test_framework = None
        self.bstack1lllll1l11l_opy_ = None
        self.bstack1l1l11l1ll1_opy_=bstack11l11ll_opy_ (u"ࠦࠧጨ")
        self.session_framework = None
        self.logger = bstack11l1l11ll1_opy_.get_logger(self.__class__.__name__, bstack11l1l11ll1_opy_.bstack1l1l11llll1_opy_())
        self.bstack1l1l111lll1_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11l11l1_opy_ = bstack1lll11l1111_opy_()
        self.bstack1l11ll11l1l_opy_ = None
        self.bstack1ll1ll1lll1_opy_ = None
        self.bstack1l11llllll1_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l11ll1111l_opy_ = []
    def bstack111ll11l1l_opy_(self):
        return os.environ.get(bstack11l11l11l1_opy_).lower().__eq__(bstack11l11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥጩ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l11l11l1_opy_, bstack11l11ll_opy_ (u"࠭ࠧጪ")).lower() in [bstack11l11ll_opy_ (u"ࠧࡵࡴࡸࡩࠬጫ"), bstack11l11ll_opy_ (u"ࠨ࠳ࠪጬ"), bstack11l11ll_opy_ (u"ࠩࡼࡩࡸ࠭ጭ")]:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡊࡴࡸࡣࡪࡰࡪࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࠦ࡭ࡰࡦࡨࠤࡩࡻࡥࠡࡶࡲࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡔࡘࡃࡆࡡࡉࡅࡑࡒࡂࡂࡅࡎࠤࡪࡴࡶࡪࡴࡲࡲࡲ࡫࡮ࡵࠢࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠦጮ"))
            os.environ[bstack11l11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡍࡘࡥࡒࡖࡐࡑࡍࡓࡍࠢጯ")] = bstack11l11ll_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦጰ")
            return False
        if bstack11l11ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪጱ") in config and str(config[bstack11l11ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫጲ")]).lower() != bstack11l11ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧጳ"):
            return False
        bstack1l1l11ll1ll_opy_ = [bstack11l11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤጴ"), bstack11l11ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢጵ")]
        bstack1l1l1ll1l11_opy_ = config.get(bstack11l11ll_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠢጶ")) in bstack1l1l11ll1ll_opy_ or os.environ.get(bstack11l11ll_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭ጷ")) in bstack1l1l11ll1ll_opy_
        os.environ[bstack11l11ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤጸ")] = str(bstack1l1l1ll1l11_opy_) # bstack1l1l1lll1l1_opy_ bstack1l11ll1l1l1_opy_ VAR to bstack1l1l1lllll1_opy_ is binary running
        return bstack1l1l1ll1l11_opy_
    def bstack11l11lll1_opy_(self):
        for event in bstack1l1l1lll111_opy_:
            bstack1lll1l1lll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1lll1l1lll_opy_.logger.debug(bstack11l11ll_opy_ (u"ࠢࡼࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࢂࠦ࠽࠿ࠢࡾࡥࡷ࡭ࡳࡾࠢࠥጹ") + str(kwargs) + bstack11l11ll_opy_ (u"ࠣࠤጺ"))
            )
        bstack1lll1l1lll_opy_.register(Events.bstack111lll11l_opy_, self.__1l1l111llll_opy_)
        bstack1lll1l1lll_opy_.register(Events.CONNECT, self.__1l1l1l11l11_opy_)
        bstack1lll1l1lll_opy_.register(Events.bstack1l111l1111_opy_, self.__1l1l111ll1l_opy_)
        bstack1lll1l1lll_opy_.register(Events.bstack1lll11l1ll_opy_, self.__1l1l111l1ll_opy_)
    def bstack1111l1ll1_opy_(self):
        return not self.bstack1l11lll1l11_opy_ and os.environ.get(bstack1l1l11l1l11_opy_, bstack11l11ll_opy_ (u"ࠤࠥጻ")) != bstack11l11ll_opy_ (u"ࠥࠦጼ")
    def is_running(self):
        if self.bstack1l11lll1l11_opy_:
            return self.bstack1l1l11l1lll_opy_
        else:
            return bool(self.bstack1l1l11lll1l_opy_)
    def bstack1l1l11l1l1l_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l11ll1111l_opy_) and cli.is_running()
    def __1l1l1111111_opy_(self, bstack1l11lllllll_opy_=10):
        if self.bstack1llll1l1ll1_opy_:
            return
        bstack1lll1l1l11_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l11111l1_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡠࠨጽ") + str(id(self)) + bstack11l11ll_opy_ (u"ࠧࡣࠠࡤࡱࡱࡲࡪࡩࡴࡪࡰࡪࠦጾ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11l11ll_opy_ (u"ࠨࡧࡳࡲࡦ࠲ࡪࡴࡡࡣ࡮ࡨࡣ࡭ࡺࡴࡱࡡࡳࡶࡴࡾࡹࠣጿ"), 0), (bstack11l11ll_opy_ (u"ࠢࡨࡴࡳࡧ࠳࡫࡮ࡢࡤ࡯ࡩࡤ࡮ࡴࡵࡲࡶࡣࡵࡸ࡯ࡹࡻࠥፀ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l11lllllll_opy_)
        self.bstack1l1l11lll1l_opy_ = channel
        self.bstack1llll1l1ll1_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1l11lll1l_opy_)
        self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡣࡰࡰࡱࡩࡨࡺࠢፁ"), datetime.now() - bstack1lll1l1l11_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l11111l1_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧ࠾ࠥ࡯ࡳࡠࡥ࡫࡭ࡱࡪ࡟ࡱࡴࡲࡧࡪࡹࡳ࠾ࠤፂ") + str(self.bstack1111l1ll1_opy_()) + bstack11l11ll_opy_ (u"ࠥࠦፃ"))
    def __1l1l111ll1l_opy_(self, event_name):
        if self.bstack1111l1ll1_opy_():
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡹࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡄࡎࡌࠦፄ"))
        self.__1l1l11lll11_opy_()
    def __1l1l111l1ll_opy_(self, event_name, bstack1l1l111111l_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack11l11ll_opy_ (u"࡙ࠧ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫ࠧፅ"))
        bstack1l1l1l11111_opy_ = Path(bstack11ll111l_opy_ (u"ࠨࡻࡴࡧ࡯ࡪ࠳ࡩ࡬ࡪࡡࡧ࡭ࡷࢃ࠯ࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࡴ࠰࡭ࡷࡴࡴࠢፆ"))
        if self.bstack1l1l11111ll_opy_ and bstack1l1l1l11111_opy_.exists():
            with open(bstack1l1l1l11111_opy_, bstack11l11ll_opy_ (u"ࠧࡳࠩፇ"), encoding=bstack11l11ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧፈ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l111lll1_opy_(bstack11l11ll_opy_ (u"ࠩࡓࡓࡘ࡚ࠧፉ"), bstack1l11lll1l1_opy_(bstack11l11111l1_opy_), data, {
                        bstack11l11ll_opy_ (u"ࠪࡥࡺࡺࡨࠨፊ"): (self.config[bstack11l11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ፋ")], self.config[bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨፌ")])
                    })
                except Exception as e:
                    logger.debug(bstack111ll111l_opy_.format(str(e)))
            bstack1l1l1l11111_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l11ll1l111_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def __1l1l111llll_opy_(self, event_name: str, data):
        from bstack_utils.bstack1l111l1l1_opy_ import bstack1lllllll1ll_opy_
        self.bstack1l1l11l1ll1_opy_, self.bstack1l1l11111ll_opy_ = bstack1l1l1llll1l_opy_(data.bs_config)
        os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡝ࡒࡊࡖࡄࡆࡑࡋ࡟ࡅࡋࡕࠫፍ")] = self.bstack1l1l11111ll_opy_
        if not self.bstack1l1l11l1ll1_opy_ or not self.bstack1l1l11111ll_opy_:
            raise ValueError(bstack11l11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡶ࡫ࡩ࡙ࠥࡄࡌࠢࡆࡐࡎࠦࡢࡪࡰࡤࡶࡾࠨፎ"))
        if self.bstack1111l1ll1_opy_():
            self.__1l1l1l11l11_opy_(event_name, bstack1l1111ll1_opy_())
            return
        try:
            bstack1lllllll1ll_opy_.end(EVENTS.bstack1ll111111_opy_.value, EVENTS.bstack1ll111111_opy_.value + bstack11l11ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣፏ"), EVENTS.bstack1ll111111_opy_.value + bstack11l11ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢፐ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11l11ll_opy_ (u"ࠥࡇࡴࡳࡰ࡭ࡧࡷࡩ࡙ࠥࡄࡌࠢࡖࡩࡹࡻࡰ࠯ࠤፑ"))
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷࠥࢁࡽࠣፒ").format(e))
        start = datetime.now()
        is_started = self.__1l1l1lll1ll_opy_()
        self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠧࡹࡰࡢࡹࡱࡣࡹ࡯࡭ࡦࠤፓ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l1111111_opy_()
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧፔ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1l1l1llll_opy_(data)
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧፕ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l11l111l_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def __1l1l1l11l11_opy_(self, event_name: str, data: bstack1l1111ll1_opy_):
        if not self.bstack1111l1ll1_opy_():
            self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨࡵ࡮࡯ࡧࡦࡸ࠿ࠦ࡮ࡰࡶࠣࡥࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷࠧፖ"))
            return
        bin_session_id = os.environ.get(bstack1l1l11l1l11_opy_)
        start = datetime.now()
        self.__1l1l1111111_opy_()
        self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࡢࡸ࡮ࡳࡥࠣፗ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11l11ll_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠦࡴࡰࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡈࡒࡉࠡࠤፘ") + str(bin_session_id) + bstack11l11ll_opy_ (u"ࠦࠧፙ"))
        start = datetime.now()
        self.__1l1l1l1111l_opy_()
        self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥፚ"), datetime.now() - start)
    def __1l11ll1lll1_opy_(self):
        if not self.bstack1llll1l1ll1_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡣࡢࡰࡱࡳࡹࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࠢࡰࡳࡩࡻ࡬ࡦࡵࠥ፛"))
            return
        bstack1l1l1ll1111_opy_ = {
            bstack11l11ll_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ፜"): (bstack1ll1ll11l11_opy_, bstack1lll1lll1l1_opy_, bstack1lll1l111l1_opy_),
            bstack11l11ll_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ፝"): (bstack1lllllll1l1_opy_, bstack1lll111l1l1_opy_, bstack1llll1l111l_opy_),
        }
        if not self.bstack1l11ll11l1l_opy_ and self.session_framework in bstack1l1l1ll1111_opy_:
            bstack1l11ll11l11_opy_, bstack1l1l1ll11l1_opy_, bstack1l11lll11l1_opy_ = bstack1l1l1ll1111_opy_[self.session_framework]
            bstack1l1l1lll11l_opy_ = bstack1l1l1ll11l1_opy_()
            self.bstack1ll1ll1lll1_opy_ = bstack1l1l1lll11l_opy_
            self.bstack1l11ll11l1l_opy_ = bstack1l11lll11l1_opy_
            self.bstack1l11ll1111l_opy_.append(bstack1l1l1lll11l_opy_)
            self.bstack1l11ll1111l_opy_.append(bstack1l11ll11l11_opy_(self.bstack1ll1ll1lll1_opy_))
        if not self.bstack1l11llllll1_opy_ and self.config_observability and self.config_observability.success: # bstack1llll11l1ll_opy_
            self.bstack1l11llllll1_opy_ = bstack1l1l1ll1l1l_opy_(self.bstack1l11ll11l1l_opy_, self.bstack1ll1ll1lll1_opy_) # bstack1l1l11ll1l1_opy_
            self.bstack1l11ll1111l_opy_.append(self.bstack1l11llllll1_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l11ll111l1_opy_(self.bstack1l11ll11l1l_opy_, self.bstack1ll1ll1lll1_opy_)
            self.bstack1l11ll1111l_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11l11ll_opy_ (u"ࠤࡶࡩࡱ࡬ࡈࡦࡣ࡯ࠦ፞"), False) == True:
            self.ai = bstack1l1ll11l1ll_opy_()
            self.bstack1l11ll1111l_opy_.append(self.ai)
        if not self.percy and self.bstack1l11lll1l1l_opy_ and self.bstack1l11lll1l1l_opy_.success:
            self.percy = bstack1l11llll111_opy_(self.bstack1l11lll1l1l_opy_)
            self.bstack1l11ll1111l_opy_.append(self.percy)
        for mod in self.bstack1l11ll1111l_opy_:
            if not mod.bstack1lll11l111l_opy_():
                mod.configure(self.bstack1llll1l1ll1_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11l11l1_opy_)
    def __1l11ll1llll_opy_(self):
        for mod in self.bstack1l11ll1111l_opy_:
            if mod.bstack1lll11l111l_opy_():
                mod.configure(self.bstack1llll1l1ll1_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l11ll111ll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def __1l1l1l1llll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l1l11lll_opy_:
            return
        self.__1l11ll1l1ll_opy_(data)
        bstack1lll1l1l11_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11l11ll_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥ፟")
        req.sdk_language = bstack11l11ll_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦ፠")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l111l111_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡡࠢ፡") + str(id(self)) + bstack11l11ll_opy_ (u"ࠨ࡝ࠡ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡵࡷࡥࡷࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧ።"))
            r = self.bstack1llll1l1ll1_opy_.StartBinSession(req)
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡴࡢࡴࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤ፣"), datetime.now() - bstack1lll1l1l11_opy_)
            os.environ[bstack1l1l11l1l11_opy_] = r.bin_session_id
            self.__1l11ll1l11l_opy_(r)
            self.__1l11ll1lll1_opy_()
            self.bstack1lll11l11l1_opy_.start()
            self.bstack1l1l1l11lll_opy_ = True
            self.logger.debug(bstack11l11ll_opy_ (u"ࠣ࡝ࠥ፤") + str(id(self)) + bstack11l11ll_opy_ (u"ࠤࡠࠤࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠢ፥"))
        except grpc.bstack1l11ll11111_opy_ as bstack1l1l1111l11_opy_:
            self.logger.error(bstack11l11ll_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡷ࡭ࡲ࡫࡯ࡦࡷࡷ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ፦") + str(bstack1l1l1111l11_opy_) + bstack11l11ll_opy_ (u"ࠦࠧ፧"))
            traceback.print_exc()
            raise bstack1l1l1111l11_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤ፨") + str(e) + bstack11l11ll_opy_ (u"ࠨࠢ፩"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11ll11ll1_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def __1l1l1l1111l_opy_(self):
        if not self.bstack1111l1ll1_opy_() or not self.cli_bin_session_id or self.bstack1l1l1l1l111_opy_:
            return
        bstack1lll1l1l11_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ፪"), bstack11l11ll_opy_ (u"ࠨ࠲ࠪ፫")))
        try:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࡞ࠦ፬") + str(id(self)) + bstack11l11ll_opy_ (u"ࠥࡡࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧ፭"))
            r = self.bstack1llll1l1ll1_opy_.ConnectBinSession(req)
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡦࡳࡳࡴࡥࡤࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣ፮"), datetime.now() - bstack1lll1l1l11_opy_)
            self.__1l11ll1l11l_opy_(r)
            self.__1l11ll1lll1_opy_()
            self.bstack1lll11l11l1_opy_.start()
            self.bstack1l1l1l1l111_opy_ = True
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡡࠢ፯") + str(id(self)) + bstack11l11ll_opy_ (u"ࠨ࡝ࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠧ፰"))
        except grpc.bstack1l11ll11111_opy_ as bstack1l1l1111l11_opy_:
            self.logger.error(bstack11l11ll_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡴࡪ࡯ࡨࡳࡪࡻࡴ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤ፱") + str(bstack1l1l1111l11_opy_) + bstack11l11ll_opy_ (u"ࠣࠤ፲"))
            traceback.print_exc()
            raise bstack1l1l1111l11_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ፳") + str(e) + bstack11l11ll_opy_ (u"ࠥࠦ፴"))
            traceback.print_exc()
            raise e
    def __1l11ll1l11l_opy_(self, r):
        self.bstack1l1l1llll11_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11l11ll_opy_ (u"ࠦࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡵࡨࡶࡻ࡫ࡲࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥ፵") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11l11ll_opy_ (u"ࠧ࡫࡭ࡱࡶࡼࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡫ࡵࡵ࡯ࡦࠥ፶"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11l11ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡪࡸࡣࡺࠢ࡬ࡷࠥࡹࡥ࡯ࡶࠣࡳࡳࡲࡹࠡࡣࡶࠤࡵࡧࡲࡵࠢࡲࡪࠥࡺࡨࡦࠢࠥࡇࡴࡴ࡮ࡦࡥࡷࡆ࡮ࡴࡓࡦࡵࡶ࡭ࡴࡴࠬࠣࠢࡤࡲࡩࠦࡴࡩ࡫ࡶࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡩࡴࠢࡤࡰࡸࡵࠠࡶࡵࡨࡨࠥࡨࡹࠡࡕࡷࡥࡷࡺࡂࡪࡰࡖࡩࡸࡹࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡦࡴࡨࡪࡴࡸࡥ࠭ࠢࡑࡳࡳ࡫ࠠࡩࡣࡱࡨࡱ࡯࡮ࡨࠢ࡬ࡷࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ፷")
        self.bstack1l11lll1l1l_opy_ = getattr(r, bstack11l11ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭፸"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ፹")] = self.config_testhub.jwt
        os.environ[bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ፺")] = self.config_testhub.build_hashed_id
    def bstack1l11llll1ll_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1l11l1lll_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l11ll1ll1l_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l11ll1ll1l_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l11llll1ll_opy_(event_name=EVENTS.bstack1l11lll1lll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def __1l1l1lll1ll_opy_(self, bstack1l11lllllll_opy_=10):
        if self.bstack1l1l11l1lll_opy_:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡷࡹࡧࡲࡵ࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠧ፻"))
            return True
        self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡸࡺࡡࡳࡶࠥ፼"))
        if os.getenv(bstack11l11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡇࡑ࡚ࠧ፽")) == bstack1l11lllll11_opy_:
            self.cli_bin_session_id = bstack1l11lllll11_opy_
            self.cli_listen_addr = bstack11l11ll_opy_ (u"ࠨࡵ࡯࡫ࡻ࠾࠴ࡺ࡭ࡱ࠱ࡶࡨࡰ࠳ࡰ࡭ࡣࡷࡪࡴࡸ࡭࠮ࠧࡶ࠲ࡸࡵࡣ࡬ࠤ፾") % (self.cli_bin_session_id)
            self.bstack1l1l11l1lll_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l11l1ll1_opy_, bstack11l11ll_opy_ (u"ࠢࡴࡦ࡮ࠦ፿")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1ll111l_opy_ compat for text=True in bstack1l11ll1ll11_opy_ python
            encoding=bstack11l11ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᎀ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l11lll1ll1_opy_ = threading.Thread(target=self.__1l11lll11ll_opy_, args=(bstack1l11lllllll_opy_,))
        bstack1l11lll1ll1_opy_.start()
        bstack1l11lll1ll1_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡵࡳࡥࡼࡴ࠺ࠡࡴࡨࡸࡺࡸ࡮ࡤࡱࡧࡩࡂࢁࡳࡦ࡮ࡩ࠲ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡸࡥࡵࡷࡵࡲࡨࡵࡤࡦࡿࠣࡳࡺࡺ࠽ࡼࡵࡨࡰ࡫࠴ࡰࡳࡱࡦࡩࡸࡹ࠮ࡴࡶࡧࡳࡺࡺ࠮ࡳࡧࡤࡨ࠭࠯ࡽࠡࡧࡵࡶࡂࠨᎁ") + str(self.process.stderr.read()) + bstack11l11ll_opy_ (u"ࠥࠦᎂ"))
        if not self.bstack1l1l11l1lll_opy_:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡠࠨᎃ") + str(id(self)) + bstack11l11ll_opy_ (u"ࠧࡣࠠࡤ࡮ࡨࡥࡳࡻࡰࠣᎄ"))
            self.__1l1l11lll11_opy_()
        self.logger.debug(bstack11l11ll_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡶࡲࡰࡥࡨࡷࡸࡥࡲࡦࡣࡧࡽ࠿ࠦࠢᎅ") + str(self.bstack1l1l11l1lll_opy_) + bstack11l11ll_opy_ (u"ࠢࠣᎆ"))
        return self.bstack1l1l11l1lll_opy_
    def __1l11lll11ll_opy_(self, bstack1l1l1111ll1_opy_=10):
        bstack1l11l1lllll_opy_ = time.time()
        while self.process and time.time() - bstack1l11l1lllll_opy_ < bstack1l1l1111ll1_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11l11ll_opy_ (u"ࠣ࡫ࡧࡁࠧᎇ") in line:
                    self.cli_bin_session_id = line.split(bstack11l11ll_opy_ (u"ࠤ࡬ࡨࡂࠨᎈ"))[-1:][0].strip()
                    self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡧࡱ࡯࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠻ࠤᎉ") + str(self.cli_bin_session_id) + bstack11l11ll_opy_ (u"ࠦࠧᎊ"))
                    continue
                if bstack11l11ll_opy_ (u"ࠧࡲࡩࡴࡶࡨࡲࡂࠨᎋ") in line:
                    self.cli_listen_addr = line.split(bstack11l11ll_opy_ (u"ࠨ࡬ࡪࡵࡷࡩࡳࡃࠢᎌ"))[-1:][0].strip()
                    self.logger.debug(bstack11l11ll_opy_ (u"ࠢࡤ࡮࡬ࡣࡱ࡯ࡳࡵࡧࡱࡣࡦࡪࡤࡳ࠼ࠥᎍ") + str(self.cli_listen_addr) + bstack11l11ll_opy_ (u"ࠣࠤᎎ"))
                    continue
                if bstack11l11ll_opy_ (u"ࠤࡳࡳࡷࡺ࠽ࠣᎏ") in line:
                    port = line.split(bstack11l11ll_opy_ (u"ࠥࡴࡴࡸࡴ࠾ࠤ᎐"))[-1:][0].strip()
                    self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡵࡵࡲࡵ࠼ࠥ᎑") + str(port) + bstack11l11ll_opy_ (u"ࠧࠨ᎒"))
                    continue
                if line.strip() == bstack1l1l1l1lll1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11l11ll_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡏࡏࡠࡕࡗࡖࡊࡇࡍࠣ᎓"), bstack11l11ll_opy_ (u"ࠢ࠲ࠤ᎔")) == bstack11l11ll_opy_ (u"ࠣ࠳ࠥ᎕"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1l11l1lll_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠤࡨࡶࡷࡵࡲ࠻ࠢࠥ᎖") + str(e) + bstack11l11ll_opy_ (u"ࠥࠦ᎗"))
        return False
    @measure(event_name=EVENTS.bstack1l1l111ll11_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def __1l1l11lll11_opy_(self):
        if self.bstack1l1l11lll1l_opy_:
            self.bstack1lll11l11l1_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l1l111l1_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l1l1l111_opy_:
                    self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠦࡸࡺ࡯ࡱࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣ᎘"), datetime.now() - start)
                else:
                    self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠧࡹࡴࡰࡲࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤ᎙"), datetime.now() - start)
            self.__1l11ll1llll_opy_()
            start = datetime.now()
            self.bstack1l1l11lll1l_opy_.close()
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠨࡤࡪࡵࡦࡳࡳࡴࡥࡤࡶࡢࡸ࡮ࡳࡥࠣ᎚"), datetime.now() - start)
            self.bstack1l1l11lll1l_opy_ = None
        if self.process:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠢࡴࡶࡲࡴࠧ᎛"))
            start = datetime.now()
            self.process.terminate()
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠣ࡭࡬ࡰࡱࡥࡴࡪ࡯ࡨࠦ᎜"), datetime.now() - start)
            self.process = None
            if self.bstack1l11lll1l11_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1l11111ll1_opy_()
                self.logger.info(
                    bstack11l11ll_opy_ (u"ࠤ࡙࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠥࡺ࡯ࠡࡸ࡬ࡩࡼࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡱࡱࡵࡸ࠱ࠦࡩ࡯ࡵ࡬࡫࡭ࡺࡳ࠭ࠢࡤࡲࡩࠦ࡭ࡢࡰࡼࠤࡲࡵࡲࡦࠢࡧࡩࡧࡻࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡱࡲࠠࡢࡶࠣࡳࡳ࡫ࠠࡱ࡮ࡤࡧࡪࠧ࡜࡯ࠤ᎝").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ᎞")] = self.config_testhub.build_hashed_id
        self.bstack1l1l11l1lll_opy_ = False
    def __1l11ll1l1ll_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11l11ll_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ᎟")] = selenium.__version__
            data.frameworks.append(bstack11l11ll_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᎠ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack11l11ll_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᎡ")] = __version__
            data.frameworks.append(bstack11l11ll_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᎢ"))
        except:
            pass
    def bstack1l1l1llllll_opy_(self, hub_url: str, platform_index: int, bstack1111l111l1_opy_: Any):
        if self.bstack1lllll1l11l_opy_:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠢࡶࡩࡹࡻࡰࠡࡵࡨࡰࡪࡴࡩࡶ࡯࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡹࡥࡵࠢࡸࡴࠧᎣ"))
            return
        try:
            bstack1lll1l1l11_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11l11ll_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᎤ")
            self.bstack1lllll1l11l_opy_ = bstack1llll1l111l_opy_(
                cli.config.get(bstack11l11ll_opy_ (u"ࠥ࡬ࡺࡨࡕࡳ࡮ࠥᎥ"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll111lll_opy_={bstack11l11ll_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡣࡴࡶࡴࡪࡱࡱࡷࡤ࡬ࡲࡰ࡯ࡢࡧࡦࡶࡳࠣᎦ"): bstack1111l111l1_opy_}
            )
            def bstack1l1l1l1l1ll_opy_(self):
                return
            if self.config.get(bstack11l11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠢᎧ"), True):
                Service.start = bstack1l1l1l1l1ll_opy_
                Service.stop = bstack1l1l1l1l1ll_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack11lll1l1l_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11l1llll_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᎨ"), datetime.now() - bstack1lll1l1l11_opy_)
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡶࡩࡱ࡫࡮ࡪࡷࡰ࠾ࠥࠨᎩ") + str(e) + bstack11l11ll_opy_ (u"ࠣࠤᎪ"))
    def bstack1l1l1ll11ll_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1l1l11l11l_opy_
            self.bstack1lllll1l11l_opy_ = bstack1lll1l111l1_opy_(
                platform_index,
                framework_name=bstack11l11ll_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᎫ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠼ࠣࠦᎬ") + str(e) + bstack11l11ll_opy_ (u"ࠦࠧᎭ"))
            pass
    def bstack1l1l1111lll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠦࡳࡦࡶࡸࡴࠥࡶࡹࡵࡧࡶࡸ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡴࡧࡷࠤࡺࡶࠢᎮ"))
            return
        if bstack11ll1l1l1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11l11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᎯ"): pytest.__version__ }, [bstack11l11ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᎰ")], self.bstack1lll11l11l1_opy_, self.bstack1llll1l1ll1_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l11lll1111_opy_({ bstack11l11ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᎱ"): pytest.__version__ }, [bstack11l11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤᎲ")], self.bstack1lll11l11l1_opy_, self.bstack1llll1l1ll1_opy_)
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶࡹࡵࡧࡶࡸ࠿ࠦࠢᎳ") + str(e) + bstack11l11ll_opy_ (u"ࠦࠧᎴ"))
        self.bstack1l11llll1l1_opy_()
    def bstack1l11llll1l1_opy_(self):
        if not self.bstack111ll11l1l_opy_():
            return
        bstack1l11l11ll_opy_ = None
        def bstack1111l1lll1_opy_(config, startdir):
            return bstack11l11ll_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࠱ࡿࠥᎵ").format(bstack11l11ll_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧᎶ"))
        def bstack1lll1lllll_opy_():
            return
        def bstack111111lll_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11l11ll_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧᎷ"):
                return bstack11l11ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢᎸ")
            else:
                return bstack1l11l11ll_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1l11l11ll_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1111l1lll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1lll1lllll_opy_
            Config.getoption = bstack111111lll_opy_
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡵࡥ࡫ࠤࡵࡿࡴࡦࡵࡷࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡦࡰࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠼ࠣࠦᎹ") + str(e) + bstack11l11ll_opy_ (u"ࠥࠦᎺ"))
    def bstack1l11lll111l_opy_(self):
        bstack111l1lll11_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack111l1lll11_opy_, dict):
            if cli.config_observability:
                bstack111l1lll11_opy_.update(
                    {bstack11l11ll_opy_ (u"ࠦࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠦᎻ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11l11ll_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹ࡟ࡵࡱࡢࡻࡷࡧࡰࠣᎼ") in accessibility.get(bstack11l11ll_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᎽ"), {}):
                    bstack1l1l1l1ll11_opy_ = accessibility.get(bstack11l11ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᎾ"))
                    bstack1l1l1l1ll11_opy_.update({ bstack11l11ll_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡗࡳ࡜ࡸࡡࡱࠤᎿ"): bstack1l1l1l1ll11_opy_.pop(bstack11l11ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࡣࡹࡵ࡟ࡸࡴࡤࡴࠧᏀ")) })
                bstack111l1lll11_opy_.update({bstack11l11ll_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥᏁ"): accessibility })
        return bstack111l1lll11_opy_
    @measure(event_name=EVENTS.bstack1l1l1l1ll1l_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def bstack1l1l1l111l1_opy_(self, bstack1l1l1l111ll_opy_: str = None, bstack1l1l1l11ll1_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1llll1l1ll1_opy_:
            return
        bstack1lll1l1l11_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1l111ll_opy_:
            req.bstack1l1l1l111ll_opy_ = bstack1l1l1l111ll_opy_
        if bstack1l1l1l11ll1_opy_:
            req.bstack1l1l1l11ll1_opy_ = bstack1l1l1l11ll1_opy_
        try:
            r = self.bstack1llll1l1ll1_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡸࡴࡶ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᏂ"), datetime.now() - bstack1lll1l1l11_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack11111l1lll_opy_(self, key: str, value: timedelta):
        tag = bstack11l11ll_opy_ (u"ࠧࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷࠧᏃ") if self.bstack1111l1ll1_opy_() else bstack11l11ll_opy_ (u"ࠨ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷࠧᏄ")
        self.bstack1l1l111lll1_opy_[bstack11l11ll_opy_ (u"ࠢ࠻ࠤᏅ").join([tag + bstack11l11ll_opy_ (u"ࠣ࠯ࠥᏆ") + str(id(self)), key])] += value
    def bstack1l11111ll1_opy_(self):
        if not os.getenv(bstack11l11ll_opy_ (u"ࠤࡇࡉࡇ࡛ࡇࡠࡒࡈࡖࡋࠨᏇ"), bstack11l11ll_opy_ (u"ࠥ࠴ࠧᏈ")) == bstack11l11ll_opy_ (u"ࠦ࠶ࠨᏉ"):
            return
        bstack1l1ll111111_opy_ = dict()
        bstack1lll11l11ll_opy_ = []
        if self.test_framework:
            bstack1lll11l11ll_opy_.extend(list(self.test_framework.bstack1lll11l11ll_opy_.values()))
        if self.bstack1lllll1l11l_opy_:
            bstack1lll11l11ll_opy_.extend(list(self.bstack1lllll1l11l_opy_.bstack1lll11l11ll_opy_.values()))
        for instance in bstack1lll11l11ll_opy_:
            if not instance.platform_index in bstack1l1ll111111_opy_:
                bstack1l1ll111111_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1ll111111_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll1111l_opy_().items():
                report[k] += v
                report[k.split(bstack11l11ll_opy_ (u"ࠧࡀࠢᏊ"))[0]] += v
        bstack1l11llll11l_opy_ = sorted([(k, v) for k, v in self.bstack1l1l111lll1_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l11l1111_opy_ = 0
        for r in bstack1l11llll11l_opy_:
            bstack1l1l11l11ll_opy_ = r[1].total_seconds()
            bstack1l1l11l1111_opy_ += bstack1l1l11l11ll_opy_
            self.logger.debug(bstack11l11ll_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡿࡷࡡ࠰࡞ࡿࡀࠦᏋ") + str(bstack1l1l11l11ll_opy_) + bstack11l11ll_opy_ (u"ࠢࠣᏌ"))
        self.logger.debug(bstack11l11ll_opy_ (u"ࠣ࠯࠰ࠦᏍ"))
        bstack1l1l1l1l11l_opy_ = []
        for platform_index, report in bstack1l1ll111111_opy_.items():
            bstack1l1l1l1l11l_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l1l1l11l_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1ll1llll1_opy_ = set()
        bstack1l1l1l1l1l1_opy_ = 0
        for r in bstack1l1l1l1l11l_opy_:
            bstack1l1l11l11ll_opy_ = r[2].total_seconds()
            bstack1l1l1l1l1l1_opy_ += bstack1l1l11l11ll_opy_
            bstack1ll1llll1_opy_.add(r[0])
            self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡷࡩࡸࡺ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠯ࡾࡶࡠ࠶࡝ࡾ࠼ࡾࡶࡠ࠷࡝ࡾ࠿ࠥᏎ") + str(bstack1l1l11l11ll_opy_) + bstack11l11ll_opy_ (u"ࠥࠦᏏ"))
        if self.bstack1111l1ll1_opy_():
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦ࠲࠳ࠢᏐ"))
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠿ࡾࡸࡴࡺࡡ࡭ࡡࡦࡰ࡮ࢃࠠࡵࡧࡶࡸ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳࡳ࠮ࡽࡶࡸࡷ࠮ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠫࢀࡁࠧᏑ") + str(bstack1l1l1l1l1l1_opy_) + bstack11l11ll_opy_ (u"ࠨࠢᏒ"))
        else:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵࡀࠦᏓ") + str(bstack1l1l11l1111_opy_) + bstack11l11ll_opy_ (u"ࠣࠤᏔ"))
        self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࠰࠱ࠧᏕ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1llll1l1ll1_opy_:
            self.logger.error(bstack11l11ll_opy_ (u"ࠥࡧࡱ࡯࡟ࡴࡧࡵࡺ࡮ࡩࡥࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡄࡣࡱࡲࡴࡺࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡶࡨࡷࡹࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࠢᏖ"))
            return None
        response = self.bstack1llll1l1ll1_opy_.TestOrchestration(request)
        self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵ࠯ࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠯ࡶࡩࡸࡹࡩࡰࡰࡀࡿࢂࠨᏗ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l1llll11_opy_(self, r):
        if r is not None and getattr(r, bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧ࠭Ꮨ"), None) and getattr(r.testhub, bstack11l11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭Ꮩ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11l11ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᏚ")))
            for bstack1l1l11lllll_opy_, err in errors.items():
                if err[bstack11l11ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭Ꮫ")] == bstack11l11ll_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᏜ"):
                    self.logger.info(err[bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᏝ")])
                else:
                    self.logger.error(err[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᏞ")])
    def bstack1l11111l1l_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()