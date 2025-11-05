# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11l111l_opy_ import bstack1lll111llll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11lll1_opy_ import bstack1l11llll11l_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll11111l_opy_ import bstack1l1ll1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1l11ll1l1ll_opy_ import bstack1l1l1l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l111_opy_ import bstack1llllllll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111111l_opy_ import bstack1ll1lllll1l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1111_opy_ import bstack1ll1ll1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1111ll_opy_ import bstack1lll1ll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1l11lll11l1_opy_ import bstack1l1l11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack111llllll_opy_ import bstack111llllll_opy_, Events, bstack11l1l11l1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l11ll11l_opy_ import bstack1l1l1l11lll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll111ll_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lll1111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll11l_opy_ import bstack1llll11111l_opy_
from bstack_utils.helper import Notset, bstack1l1l1llll11_opy_, get_cli_dir, bstack1l1l1l11ll1_opy_, bstack11l111ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll1111l111_opy_ import bstack1ll11l111ll_opy_
from browserstack_sdk.sdk_cli.utils.bstack11l1llllll_opy_ import bstack1l1lllllll_opy_
from bstack_utils.helper import Notset, bstack1l1l1llll11_opy_, get_cli_dir, bstack1l1l1l11ll1_opy_, bstack11l111ll1l_opy_, bstack1111ll1lll_opy_, bstack1lll1111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1l1ll1l_opy_, bstack1lll1ll1l1l_opy_, bstack1ll111lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1llll111l1l_opy_, bstack1lllllll1l1_opy_, bstack1llllll1111_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1l1l1ll11_opy_ import bstack1ll11llll_opy_
from bstack_utils import bstack111111l11l_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111111l11_opy_, bstack11llllll1l_opy_
logger = bstack111111l11l_opy_.get_logger(__name__, bstack111111l11l_opy_.bstack1l1l11l111l_opy_())
def bstack1l1l111llll_opy_(bs_config):
    bstack1l1l1ll1ll1_opy_ = None
    bstack1l11lll1l11_opy_ = None
    try:
        bstack1l11lll1l11_opy_ = get_cli_dir()
        bstack1l1l1ll1ll1_opy_ = bstack1l1l1l11ll1_opy_(bstack1l11lll1l11_opy_)
        bstack1l1l11111l1_opy_ = bstack1l1l1llll11_opy_(bstack1l1l1ll1ll1_opy_, bstack1l11lll1l11_opy_, bs_config)
        bstack1l1l1ll1ll1_opy_ = bstack1l1l11111l1_opy_ if bstack1l1l11111l1_opy_ else bstack1l1l1ll1ll1_opy_
        if not bstack1l1l1ll1ll1_opy_:
            raise ValueError(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠥጜ"))
    except Exception as ex:
        logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡭ࡣࡷࡩࡸࡺࠠࡣ࡫ࡱࡥࡷࡿࠠࡼࡿࠥጝ").format(ex))
        bstack1l1l1ll1ll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠦጞ"))
        if bstack1l1l1ll1ll1_opy_:
            logger.debug(bstack11111_opy_ (u"ࠤࡉࡥࡱࡲࡩ࡯ࡩࠣࡦࡦࡩ࡫ࠡࡶࡲࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠠࡧࡴࡲࡱࠥ࡫࡮ࡷ࡫ࡵࡳࡳࡳࡥ࡯ࡶ࠽ࠤࠧጟ") + str(bstack1l1l1ll1ll1_opy_) + bstack11111_opy_ (u"ࠥࠦጠ"))
        else:
            logger.debug(bstack11111_opy_ (u"ࠦࡓࡵࠠࡷࡣ࡯࡭ࡩࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࡪࡴࡶࡪࡴࡲࡲࡲ࡫࡮ࡵ࠽ࠣࡷࡪࡺࡵࡱࠢࡰࡥࡾࠦࡢࡦࠢ࡬ࡲࡨࡵ࡭ࡱ࡮ࡨࡸࡪ࠴ࠢጡ"))
    return bstack1l1l1ll1ll1_opy_, bstack1l11lll1l11_opy_
bstack1l1l1111l1l_opy_ = bstack11111_opy_ (u"ࠧ࠿࠹࠺࠻ࠥጢ")
bstack1l1l1l1ll11_opy_ = bstack11111_opy_ (u"ࠨࡲࡦࡣࡧࡽࠧጣ")
bstack1l11ll11111_opy_ = bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡔࡇࡖࡗࡎࡕࡎࡠࡋࡇࠦጤ")
bstack1l1l1l1llll_opy_ = bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡎࡌࡗ࡙ࡋࡎࡠࡃࡇࡈࡗࠨጥ")
bstack1ll111111l_opy_ = bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠧጦ")
bstack1l11ll1llll_opy_ = re.compile(bstack11111_opy_ (u"ࡵࠦ࠭ࡅࡩࠪ࠰࠭ࠬࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡿࡆࡘ࠯࠮ࠫࠤጧ"))
bstack1l1l11l1ll1_opy_ = bstack11111_opy_ (u"ࠦࡩ࡫ࡶࡦ࡮ࡲࡴࡲ࡫࡮ࡵࠤጨ")
bstack1l1l1l11111_opy_ = bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡕࡒࡄࡇࡢࡊࡆࡒࡌࡃࡃࡆࡏࠧጩ")
bstack1l1l1ll11l1_opy_ = [
    Events.bstack1l1lllll1_opy_,
    Events.CONNECT,
    Events.bstack111l1ll1ll_opy_,
]
class SDKCLI:
    _1ll1l1lll11_opy_ = None
    process: Union[None, Any]
    bstack1l11ll1l1l1_opy_: bool
    bstack1l11ll1ll1l_opy_: bool
    bstack1l1l11l1l11_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l11lllll1l_opy_: Union[None, grpc.Channel]
    bstack1l11l1llll1_opy_: str
    test_framework: TestFramework
    bstack1llll1l1l11_opy_: bstack1lll1111l1l_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l11ll1ll_opy_: bstack1l1l11l11l1_opy_
    accessibility: bstack1l11llll11l_opy_
    bstack11l1llllll_opy_: bstack1l1lllllll_opy_
    ai: bstack1l1ll1111ll_opy_
    bstack1l1l1ll1l1l_opy_: bstack1l1l1l11l1l_opy_
    bstack1l11ll1ll11_opy_: List[bstack1llll111ll1_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l1lllll1_opy_: Any
    bstack1l1l1ll11ll_opy_: Dict[str, timedelta]
    bstack1l11llll111_opy_: str
    bstack1lll11l111l_opy_: bstack1lll111llll_opy_
    def __new__(cls):
        if not cls._1ll1l1lll11_opy_:
            cls._1ll1l1lll11_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1l1lll11_opy_
    def __init__(self):
        self.process = None
        self.bstack1l11ll1l1l1_opy_ = False
        self.bstack1l11lllll1l_opy_ = None
        self.bstack1llll1ll1ll_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l1l1llll_opy_, None)
        self.bstack1l1l1111111_opy_ = os.environ.get(bstack1l11ll11111_opy_, bstack11111_opy_ (u"ࠨࠢጪ")) == bstack11111_opy_ (u"ࠢࠣጫ")
        self.bstack1l11ll1ll1l_opy_ = False
        self.bstack1l1l11l1l11_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l1lllll1_opy_ = None
        self.test_framework = None
        self.bstack1llll1l1l11_opy_ = None
        self.bstack1l11l1llll1_opy_=bstack11111_opy_ (u"ࠣࠤጬ")
        self.session_framework = None
        self.logger = bstack111111l11l_opy_.get_logger(self.__class__.__name__, bstack111111l11l_opy_.bstack1l1l11l111l_opy_())
        self.bstack1l1l1ll11ll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11l111l_opy_ = bstack1lll111llll_opy_()
        self.bstack1l1l11ll1l1_opy_ = None
        self.bstack1ll1ll1ll1l_opy_ = None
        self.bstack1l1l11ll1ll_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l11ll1ll11_opy_ = []
    def bstack1l1lll1ll_opy_(self):
        return os.environ.get(bstack1ll111111l_opy_).lower().__eq__(bstack11111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢጭ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l1l11111_opy_, bstack11111_opy_ (u"ࠪࠫጮ")).lower() in [bstack11111_opy_ (u"ࠫࡹࡸࡵࡦࠩጯ"), bstack11111_opy_ (u"ࠬ࠷ࠧጰ"), bstack11111_opy_ (u"࠭ࡹࡦࡵࠪጱ")]:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡇࡱࡵࡧ࡮ࡴࡧࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡱࡴࡪࡥࠡࡦࡸࡩࠥࡺ࡯ࠡࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡑࡕࡇࡊࡥࡆࡂࡎࡏࡆࡆࡉࡋࠡࡧࡱࡺ࡮ࡸ࡯࡯࡯ࡨࡲࡹࠦࡶࡢࡴ࡬ࡥࡧࡲࡥࠣጲ"))
            os.environ[bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦጳ")] = bstack11111_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣጴ")
            return False
        if bstack11111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧጵ") in config and str(config[bstack11111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨጶ")]).lower() != bstack11111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫጷ"):
            return False
        bstack1l1l111l11l_opy_ = [bstack11111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨጸ"), bstack11111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦጹ")]
        bstack1l1l1ll1l11_opy_ = config.get(bstack11111_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦጺ")) in bstack1l1l111l11l_opy_ or os.environ.get(bstack11111_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪጻ")) in bstack1l1l111l11l_opy_
        os.environ[bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨጼ")] = str(bstack1l1l1ll1l11_opy_) # bstack1l11ll1lll1_opy_ bstack1l11ll111ll_opy_ VAR to bstack1l11ll1l111_opy_ is binary running
        return bstack1l1l1ll1l11_opy_
    def bstack11ll11ll1l_opy_(self):
        for event in bstack1l1l1ll11l1_opy_:
            bstack111llllll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack111llllll_opy_.logger.debug(bstack11111_opy_ (u"ࠦࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠣࡁࡃࠦࡻࡢࡴࡪࡷࢂࠦࠢጽ") + str(kwargs) + bstack11111_opy_ (u"ࠧࠨጾ"))
            )
        bstack111llllll_opy_.register(Events.bstack1l1lllll1_opy_, self.__1l11lll111l_opy_)
        bstack111llllll_opy_.register(Events.CONNECT, self.__1l1l1lll11l_opy_)
        bstack111llllll_opy_.register(Events.bstack111l1ll1ll_opy_, self.__1l11lll1111_opy_)
        bstack111llllll_opy_.register(Events.bstack1l1ll1111_opy_, self.__1l1l1l1l1ll_opy_)
    def bstack11l11ll11l_opy_(self):
        return not self.bstack1l1l1111111_opy_ and os.environ.get(bstack1l11ll11111_opy_, bstack11111_opy_ (u"ࠨࠢጿ")) != bstack11111_opy_ (u"ࠢࠣፀ")
    def is_running(self):
        if self.bstack1l1l1111111_opy_:
            return self.bstack1l11ll1l1l1_opy_
        else:
            return bool(self.bstack1l11lllll1l_opy_)
    def bstack1l1l1l1l1l1_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l11ll1ll11_opy_) and cli.is_running()
    def __1l11lllll11_opy_(self, bstack1l1l1ll1111_opy_=10):
        if self.bstack1llll1ll1ll_opy_:
            return
        bstack11lll11111_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l1l1llll_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11111_opy_ (u"ࠣ࡝ࠥፁ") + str(id(self)) + bstack11111_opy_ (u"ࠤࡠࠤࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡴࡧࠣፂ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠯ࡧࡱࡥࡧࡲࡥࡠࡪࡷࡸࡵࡥࡰࡳࡱࡻࡽࠧፃ"), 0), (bstack11111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠰ࡨࡲࡦࡨ࡬ࡦࡡ࡫ࡸࡹࡶࡳࡠࡲࡵࡳࡽࡿࠢፄ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l1ll1111_opy_)
        self.bstack1l11lllll1l_opy_ = channel
        self.bstack1llll1ll1ll_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l11lllll1l_opy_)
        self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡧࡴࡴ࡮ࡦࡥࡷࠦፅ"), datetime.now() - bstack11lll11111_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l1l1llll_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11111_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤ࠻ࠢ࡬ࡷࡤࡩࡨࡪ࡮ࡧࡣࡵࡸ࡯ࡤࡧࡶࡷࡂࠨፆ") + str(self.bstack11l11ll11l_opy_()) + bstack11111_opy_ (u"ࠢࠣፇ"))
    def __1l11lll1111_opy_(self, event_name):
        if self.bstack11l11ll11l_opy_():
            self.logger.debug(bstack11111_opy_ (u"ࠣࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡶࡸࡴࡶࡰࡪࡰࡪࠤࡈࡒࡉࠣፈ"))
        self.__1l1l11ll111_opy_()
    def __1l1l1l1l1ll_opy_(self, event_name, bstack1l1l1111ll1_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack11111_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠤፉ"))
        bstack1l1l11l1lll_opy_ = Path(bstack1lll1l1l111_opy_ (u"ࠥࡿࡸ࡫࡬ࡧ࠰ࡦࡰ࡮ࡥࡤࡪࡴࢀ࠳ࡺࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࡸ࠴ࡪࡴࡱࡱࠦፊ"))
        if self.bstack1l11lll1l11_opy_ and bstack1l1l11l1lll_opy_.exists():
            with open(bstack1l1l11l1lll_opy_, bstack11111_opy_ (u"ࠫࡷ࠭ፋ"), encoding=bstack11111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫፌ")) as fp:
                data = json.load(fp)
                try:
                    bstack1111ll1lll_opy_(bstack11111_opy_ (u"࠭ࡐࡐࡕࡗࠫፍ"), bstack1ll11llll_opy_(bstack1l1l1l11l_opy_), data, {
                        bstack11111_opy_ (u"ࠧࡢࡷࡷ࡬ࠬፎ"): (self.config[bstack11111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪፏ")], self.config[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬፐ")])
                    })
                except Exception as e:
                    logger.debug(bstack11llllll1l_opy_.format(str(e)))
            bstack1l1l11l1lll_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l111lll1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1l11lll111l_opy_(self, event_name: str, data):
        from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
        self.bstack1l11l1llll1_opy_, self.bstack1l11lll1l11_opy_ = bstack1l1l111llll_opy_(data.bs_config)
        os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡ࡚ࡖࡎ࡚ࡁࡃࡎࡈࡣࡉࡏࡒࠨፑ")] = self.bstack1l11lll1l11_opy_
        if not self.bstack1l11l1llll1_opy_ or not self.bstack1l11lll1l11_opy_:
            raise ValueError(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡺࡨࡦࠢࡖࡈࡐࠦࡃࡍࡋࠣࡦ࡮ࡴࡡࡳࡻࠥፒ"))
        if self.bstack11l11ll11l_opy_():
            self.__1l1l1lll11l_opy_(event_name, bstack11l1l11l1_opy_())
            return
        try:
            bstack1llll1ll1l1_opy_.end(EVENTS.bstack1l1l111l1l_opy_.value, EVENTS.bstack1l1l111l1l_opy_.value + bstack11111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧፓ"), EVENTS.bstack1l1l111l1l_opy_.value + bstack11111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦፔ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11111_opy_ (u"ࠢࡄࡱࡰࡴࡱ࡫ࡴࡦࠢࡖࡈࡐࠦࡓࡦࡶࡸࡴ࠳ࠨፕ"))
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡾࢁࠧፖ").format(e))
        start = datetime.now()
        is_started = self.__1l1l11l11ll_opy_()
        self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠤࡶࡴࡦࡽ࡮ࡠࡶ࡬ࡱࡪࠨፗ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l11lllll11_opy_()
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤፘ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1l1l111l1_opy_(data)
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤፙ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l1lll111_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1l1l1lll11l_opy_(self, event_name: str, data: bstack11l1l11l1_opy_):
        if not self.bstack11l11ll11l_opy_():
            self.logger.debug(bstack11111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥࡲࡲࡳ࡫ࡣࡵ࠼ࠣࡲࡴࡺࠠࡢࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴࠤፚ"))
            return
        bin_session_id = os.environ.get(bstack1l11ll11111_opy_)
        start = datetime.now()
        self.__1l11lllll11_opy_()
        self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧ፛"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11111_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦࠣࡸࡴࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡅࡏࡍࠥࠨ፜") + str(bin_session_id) + bstack11111_opy_ (u"ࠣࠤ፝"))
        start = datetime.now()
        self.__1l1l1ll111l_opy_()
        self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢ፞"), datetime.now() - start)
    def __1l1l1l11l11_opy_(self):
        if not self.bstack1llll1ll1ll_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡧࡦࡴ࡮ࡰࡶࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࠦ࡭ࡰࡦࡸࡰࡪࡹࠢ፟"))
            return
        bstack1l11ll1l11l_opy_ = {
            bstack11111_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ፠"): (bstack1ll1ll1l1ll_opy_, bstack1lll1ll1lll_opy_, bstack1llll11111l_opy_),
            bstack11111_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ፡"): (bstack1llllllll1l_opy_, bstack1ll1lllll1l_opy_, bstack1lllll1111l_opy_),
        }
        if not self.bstack1l1l11ll1l1_opy_ and self.session_framework in bstack1l11ll1l11l_opy_:
            bstack1l1l11llll1_opy_, bstack1l1l111l1l1_opy_, bstack1l1l1lll1ll_opy_ = bstack1l11ll1l11l_opy_[self.session_framework]
            bstack1l11llllll1_opy_ = bstack1l1l111l1l1_opy_()
            self.bstack1ll1ll1ll1l_opy_ = bstack1l11llllll1_opy_
            self.bstack1l1l11ll1l1_opy_ = bstack1l1l1lll1ll_opy_
            self.bstack1l11ll1ll11_opy_.append(bstack1l11llllll1_opy_)
            self.bstack1l11ll1ll11_opy_.append(bstack1l1l11llll1_opy_(self.bstack1ll1ll1ll1l_opy_))
        if not self.bstack1l1l11ll1ll_opy_ and self.config_observability and self.config_observability.success: # bstack1llll11l1ll_opy_
            self.bstack1l1l11ll1ll_opy_ = bstack1l1l11l11l1_opy_(self.bstack1l1l11ll1l1_opy_, self.bstack1ll1ll1ll1l_opy_) # bstack1l11l1lllll_opy_
            self.bstack1l11ll1ll11_opy_.append(self.bstack1l1l11ll1ll_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l11llll11l_opy_(self.bstack1l1l11ll1l1_opy_, self.bstack1ll1ll1ll1l_opy_)
            self.bstack1l11ll1ll11_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11111_opy_ (u"ࠨࡳࡦ࡮ࡩࡌࡪࡧ࡬ࠣ።"), False) == True:
            self.ai = bstack1l1ll1111ll_opy_()
            self.bstack1l11ll1ll11_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l1lllll1_opy_ and self.bstack1l1l1lllll1_opy_.success:
            self.percy = bstack1l1l1l11l1l_opy_(self.bstack1l1l1lllll1_opy_)
            self.bstack1l11ll1ll11_opy_.append(self.percy)
        for mod in self.bstack1l11ll1ll11_opy_:
            if not mod.bstack1lll11l1111_opy_():
                mod.configure(self.bstack1llll1ll1ll_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11l111l_opy_)
    def __1l1l11lll11_opy_(self):
        for mod in self.bstack1l11ll1ll11_opy_:
            if mod.bstack1lll11l1111_opy_():
                mod.configure(self.bstack1llll1ll1ll_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l1l1llllll_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1l1l1l111l1_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l11ll1ll1l_opy_:
            return
        self.__1l1l1llll1l_opy_(data)
        bstack11lll11111_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11111_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢ፣")
        req.sdk_language = bstack11111_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣ፤")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l11ll1llll_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11111_opy_ (u"ࠤ࡞ࠦ፥") + str(id(self)) + bstack11111_opy_ (u"ࠥࡡࠥࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡹࡴࡢࡴࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤ፦"))
            r = self.bstack1llll1ll1ll_opy_.StartBinSession(req)
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡸࡦࡸࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨ፧"), datetime.now() - bstack11lll11111_opy_)
            os.environ[bstack1l11ll11111_opy_] = r.bin_session_id
            self.__1l11lll1ll1_opy_(r)
            self.__1l1l1l11l11_opy_()
            self.bstack1lll11l111l_opy_.start()
            self.bstack1l11ll1ll1l_opy_ = True
            self.logger.debug(bstack11111_opy_ (u"ࠧࡡࠢ፨") + str(id(self)) + bstack11111_opy_ (u"ࠨ࡝ࠡ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠦ፩"))
        except grpc.bstack1l1l111l111_opy_ as bstack1l11lll1l1l_opy_:
            self.logger.error(bstack11111_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡴࡪ࡯ࡨࡳࡪࡻࡴ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤ፪") + str(bstack1l11lll1l1l_opy_) + bstack11111_opy_ (u"ࠣࠤ፫"))
            traceback.print_exc()
            raise bstack1l11lll1l1l_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ፬") + str(e) + bstack11111_opy_ (u"ࠥࠦ፭"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l11lll1l_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1l1l1ll111l_opy_(self):
        if not self.bstack11l11ll11l_opy_() or not self.cli_bin_session_id or self.bstack1l1l11l1l11_opy_:
            return
        bstack11lll11111_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ፮"), bstack11111_opy_ (u"ࠬ࠶ࠧ፯")))
        try:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡛ࠣ፰") + str(id(self)) + bstack11111_opy_ (u"ࠢ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤ፱"))
            r = self.bstack1llll1ll1ll_opy_.ConnectBinSession(req)
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡣࡰࡰࡱࡩࡨࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧ፲"), datetime.now() - bstack11lll11111_opy_)
            self.__1l11lll1ll1_opy_(r)
            self.__1l1l1l11l11_opy_()
            self.bstack1lll11l111l_opy_.start()
            self.bstack1l1l11l1l11_opy_ = True
            self.logger.debug(bstack11111_opy_ (u"ࠤ࡞ࠦ፳") + str(id(self)) + bstack11111_opy_ (u"ࠥࡡࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠤ፴"))
        except grpc.bstack1l1l111l111_opy_ as bstack1l11lll1l1l_opy_:
            self.logger.error(bstack11111_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡸ࡮ࡳࡥࡰࡧࡸࡸ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ፵") + str(bstack1l11lll1l1l_opy_) + bstack11111_opy_ (u"ࠧࠨ፶"))
            traceback.print_exc()
            raise bstack1l11lll1l1l_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥ፷") + str(e) + bstack11111_opy_ (u"ࠢࠣ፸"))
            traceback.print_exc()
            raise e
    def __1l11lll1ll1_opy_(self, r):
        self.bstack1l1l1ll1lll_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11111_opy_ (u"ࠣࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡹࡥࡳࡸࡨࡶࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢ፹") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11111_opy_ (u"ࠤࡨࡱࡵࡺࡹࠡࡥࡲࡲ࡫࡯ࡧࠡࡨࡲࡹࡳࡪࠢ፺"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡧࡵࡧࡾࠦࡩࡴࠢࡶࡩࡳࡺࠠࡰࡰ࡯ࡽࠥࡧࡳࠡࡲࡤࡶࡹࠦ࡯ࡧࠢࡷ࡬ࡪࠦࠢࡄࡱࡱࡲࡪࡩࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱ࠰ࠧࠦࡡ࡯ࡦࠣࡸ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣ࡭ࡸࠦࡡ࡭ࡵࡲࠤࡺࡹࡥࡥࠢࡥࡽ࡙ࠥࡴࡢࡴࡷࡆ࡮ࡴࡓࡦࡵࡶ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬ࡪࡸࡥࡧࡱࡵࡩ࠱ࠦࡎࡰࡰࡨࠤ࡭ࡧ࡮ࡥ࡮࡬ࡲ࡬ࠦࡩࡴࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ፻")
        self.bstack1l1l1lllll1_opy_ = getattr(r, bstack11111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ፼"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ፽")] = self.config_testhub.jwt
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ፾")] = self.config_testhub.build_hashed_id
    def bstack1l11ll11lll_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l11ll1l1l1_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l11lllllll_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l11lllllll_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l11ll11lll_opy_(event_name=EVENTS.bstack1l1l1l1111l_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1l1l11l11ll_opy_(self, bstack1l1l1ll1111_opy_=10):
        if self.bstack1l11ll1l1l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡴࡶࡤࡶࡹࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡴࡸࡲࡳ࡯࡮ࡨࠤ፿"))
            return True
        self.logger.debug(bstack11111_opy_ (u"ࠣࡵࡷࡥࡷࡺࠢᎀ"))
        if os.getenv(bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡋࡎࡗࠤᎁ")) == bstack1l1l11l1ll1_opy_:
            self.cli_bin_session_id = bstack1l1l11l1ll1_opy_
            self.cli_listen_addr = bstack11111_opy_ (u"ࠥࡹࡳ࡯ࡸ࠻࠱ࡷࡱࡵ࠵ࡳࡥ࡭࠰ࡴࡱࡧࡴࡧࡱࡵࡱ࠲ࠫࡳ࠯ࡵࡲࡧࡰࠨᎂ") % (self.cli_bin_session_id)
            self.bstack1l11ll1l1l1_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l11l1llll1_opy_, bstack11111_opy_ (u"ࠦࡸࡪ࡫ࠣᎃ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1lll1l1_opy_ compat for text=True in bstack1l11llll1ll_opy_ python
            encoding=bstack11111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᎄ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l11ll11ll1_opy_ = threading.Thread(target=self.__1l1l11lllll_opy_, args=(bstack1l1l1ll1111_opy_,))
        bstack1l11ll11ll1_opy_.start()
        bstack1l11ll11ll1_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡹࡰࡢࡹࡱ࠾ࠥࡸࡥࡵࡷࡵࡲࡨࡵࡤࡦ࠿ࡾࡷࡪࡲࡦ࠯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡵࡩࡹࡻࡲ࡯ࡥࡲࡨࡪࢃࠠࡰࡷࡷࡁࢀࡹࡥ࡭ࡨ࠱ࡴࡷࡵࡣࡦࡵࡶ࠲ࡸࡺࡤࡰࡷࡷ࠲ࡷ࡫ࡡࡥࠪࠬࢁࠥ࡫ࡲࡳ࠿ࠥᎅ") + str(self.process.stderr.read()) + bstack11111_opy_ (u"ࠢࠣᎆ"))
        if not self.bstack1l11ll1l1l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠣ࡝ࠥᎇ") + str(id(self)) + bstack11111_opy_ (u"ࠤࡠࠤࡨࡲࡥࡢࡰࡸࡴࠧᎈ"))
            self.__1l1l11ll111_opy_()
        self.logger.debug(bstack11111_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡳࡶࡴࡩࡥࡴࡵࡢࡶࡪࡧࡤࡺ࠼ࠣࠦᎉ") + str(self.bstack1l11ll1l1l1_opy_) + bstack11111_opy_ (u"ࠦࠧᎊ"))
        return self.bstack1l11ll1l1l1_opy_
    def __1l1l11lllll_opy_(self, bstack1l1l1l1l11l_opy_=10):
        bstack1l11ll11l11_opy_ = time.time()
        while self.process and time.time() - bstack1l11ll11l11_opy_ < bstack1l1l1l1l11l_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11111_opy_ (u"ࠧ࡯ࡤ࠾ࠤᎋ") in line:
                    self.cli_bin_session_id = line.split(bstack11111_opy_ (u"ࠨࡩࡥ࠿ࠥᎌ"))[-1:][0].strip()
                    self.logger.debug(bstack11111_opy_ (u"ࠢࡤ࡮࡬ࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨ࠿ࠨᎍ") + str(self.cli_bin_session_id) + bstack11111_opy_ (u"ࠣࠤᎎ"))
                    continue
                if bstack11111_opy_ (u"ࠤ࡯࡭ࡸࡺࡥ࡯࠿ࠥᎏ") in line:
                    self.cli_listen_addr = line.split(bstack11111_opy_ (u"ࠥࡰ࡮ࡹࡴࡦࡰࡀࠦ᎐"))[-1:][0].strip()
                    self.logger.debug(bstack11111_opy_ (u"ࠦࡨࡲࡩࡠ࡮࡬ࡷࡹ࡫࡮ࡠࡣࡧࡨࡷࡀࠢ᎑") + str(self.cli_listen_addr) + bstack11111_opy_ (u"ࠧࠨ᎒"))
                    continue
                if bstack11111_opy_ (u"ࠨࡰࡰࡴࡷࡁࠧ᎓") in line:
                    port = line.split(bstack11111_opy_ (u"ࠢࡱࡱࡵࡸࡂࠨ᎔"))[-1:][0].strip()
                    self.logger.debug(bstack11111_opy_ (u"ࠣࡲࡲࡶࡹࡀࠢ᎕") + str(port) + bstack11111_opy_ (u"ࠤࠥ᎖"))
                    continue
                if line.strip() == bstack1l1l1l1ll11_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11111_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡌࡓࡤ࡙ࡔࡓࡇࡄࡑࠧ᎗"), bstack11111_opy_ (u"ࠦ࠶ࠨ᎘")) == bstack11111_opy_ (u"ࠧ࠷ࠢ᎙"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l11ll1l1l1_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡥࡳࡴࡲࡶ࠿ࠦࠢ᎚") + str(e) + bstack11111_opy_ (u"ࠢࠣ᎛"))
        return False
    @measure(event_name=EVENTS.bstack1l1l111ll1l_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1l1l11ll111_opy_(self):
        if self.bstack1l11lllll1l_opy_:
            self.bstack1lll11l111l_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l111111l_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l11l1l11_opy_:
                    self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠣࡵࡷࡳࡵࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧ᎜"), datetime.now() - start)
                else:
                    self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠤࡶࡸࡴࡶ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨ᎝"), datetime.now() - start)
            self.__1l1l11lll11_opy_()
            start = datetime.now()
            self.bstack1l11lllll1l_opy_.close()
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠥࡨ࡮ࡹࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧ᎞"), datetime.now() - start)
            self.bstack1l11lllll1l_opy_ = None
        if self.process:
            self.logger.debug(bstack11111_opy_ (u"ࠦࡸࡺ࡯ࡱࠤ᎟"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠧࡱࡩ࡭࡮ࡢࡸ࡮ࡳࡥࠣᎠ"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l1111111_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack111l1111ll_opy_()
                self.logger.info(
                    bstack11111_opy_ (u"ࠨࡖࡪࡵ࡬ࡸࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠢࡷࡳࠥࡼࡩࡦࡹࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡵࡵࡲࡵ࠮ࠣ࡭ࡳࡹࡩࡨࡪࡷࡷ࠱ࠦࡡ࡯ࡦࠣࡱࡦࡴࡹࠡ࡯ࡲࡶࡪࠦࡤࡦࡤࡸ࡫࡬࡯࡮ࡨࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮࡯ࠤࡦࡺࠠࡰࡰࡨࠤࡵࡲࡡࡤࡧࠤࡠࡳࠨᎡ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭Ꭲ")] = self.config_testhub.build_hashed_id
        self.bstack1l11ll1l1l1_opy_ = False
    def __1l1l1llll1l_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11111_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥᎣ")] = selenium.__version__
            data.frameworks.append(bstack11111_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᎤ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack11111_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᎥ")] = __version__
            data.frameworks.append(bstack11111_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᎦ"))
        except:
            pass
    def bstack1l1l1l1l111_opy_(self, hub_url: str, platform_index: int, bstack1lllll11ll_opy_: Any):
        if self.bstack1llll1l1l11_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠦࡳࡦࡶࡸࡴࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡶࡩࡹࠦࡵࡱࠤᎧ"))
            return
        try:
            bstack11lll11111_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11111_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᎨ")
            self.bstack1llll1l1l11_opy_ = bstack1lllll1111l_opy_(
                cli.config.get(bstack11111_opy_ (u"ࠢࡩࡷࡥ࡙ࡷࡲࠢᎩ"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll1lllll_opy_={bstack11111_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡩࡶࡴࡳ࡟ࡤࡣࡳࡷࠧᎪ"): bstack1lllll11ll_opy_}
            )
            def bstack1l1l11l1111_opy_(self):
                return
            if self.config.get(bstack11111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠦᎫ"), True):
                Service.start = bstack1l1l11l1111_opy_
                Service.stop = bstack1l1l11l1111_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack1l1lllllll_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11l111ll_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᎬ"), datetime.now() - bstack11lll11111_opy_)
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠻ࠢࠥᎭ") + str(e) + bstack11111_opy_ (u"ࠧࠨᎮ"))
    def bstack1l11ll11l1l_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack11ll1l11l_opy_
            self.bstack1llll1l1l11_opy_ = bstack1llll11111l_opy_(
                platform_index,
                framework_name=bstack11111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᎯ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡀࠠࠣᎰ") + str(e) + bstack11111_opy_ (u"ࠣࠤᎱ"))
            pass
    def bstack1l1l1l111ll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠣࡷࡪࡺࡵࡱࠢࡳࡽࡹ࡫ࡳࡵ࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡸ࡫ࡴࠡࡷࡳࠦᎲ"))
            return
        if bstack11l111ll1l_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᎳ"): pytest.__version__ }, [bstack11111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣᎴ")], self.bstack1lll11l111l_opy_, self.bstack1llll1ll1ll_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l1l1l11lll_opy_({ bstack11111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᎵ"): pytest.__version__ }, [bstack11111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᎶ")], self.bstack1lll11l111l_opy_, self.bstack1llll1ll1ll_opy_)
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡽࡹ࡫ࡳࡵ࠼ࠣࠦᎷ") + str(e) + bstack11111_opy_ (u"ࠣࠤᎸ"))
        self.bstack1l11lll1lll_opy_()
    def bstack1l11lll1lll_opy_(self):
        if not self.bstack1l1lll1ll_opy_():
            return
        bstack11l11ll1l1_opy_ = None
        def bstack1llll1lll1_opy_(config, startdir):
            return bstack11111_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿ࠵ࢃࠢᎹ").format(bstack11111_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤᎺ"))
        def bstack1ll1l1l1l_opy_():
            return
        def bstack11llll11l1_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11111_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫᎻ"):
                return bstack11111_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦᎼ")
            else:
                return bstack11l11ll1l1_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack11l11ll1l1_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1llll1lll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll1l1l1l_opy_
            Config.getoption = bstack11llll11l1_opy_
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡹࡩࡨࠡࡲࡼࡸࡪࡹࡴࠡࡵࡨࡰࡪࡴࡩࡶ࡯ࠣࡪࡴࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡀࠠࠣᎽ") + str(e) + bstack11111_opy_ (u"ࠢࠣᎾ"))
    def bstack1l1l1111lll_opy_(self):
        bstack11lll11l11_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack11lll11l11_opy_, dict):
            if cli.config_observability:
                bstack11lll11l11_opy_.update(
                    {bstack11111_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣᎿ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11111_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࡣࡹࡵ࡟ࡸࡴࡤࡴࠧᏀ") in accessibility.get(bstack11111_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦᏁ"), {}):
                    bstack1l11ll111l1_opy_ = accessibility.get(bstack11111_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᏂ"))
                    bstack1l11ll111l1_opy_.update({ bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࡔࡰ࡙ࡵࡥࡵࠨᏃ"): bstack1l11ll111l1_opy_.pop(bstack11111_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡠࡶࡲࡣࡼࡸࡡࡱࠤᏄ")) })
                bstack11lll11l11_opy_.update({bstack11111_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢᏅ"): accessibility })
        return bstack11lll11l11_opy_
    @measure(event_name=EVENTS.bstack1l1l11111ll_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1l1l111111l_opy_(self, bstack1l1l1111l11_opy_: str = None, bstack1l11lll11ll_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1llll1ll1ll_opy_:
            return
        bstack11lll11111_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1111l11_opy_:
            req.bstack1l1l1111l11_opy_ = bstack1l1l1111l11_opy_
        if bstack1l11lll11ll_opy_:
            req.bstack1l11lll11ll_opy_ = bstack1l11lll11ll_opy_
        try:
            r = self.bstack1llll1ll1ll_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡵࡱࡳࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᏆ"), datetime.now() - bstack11lll11111_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1llll1l111_opy_(self, key: str, value: timedelta):
        tag = bstack11111_opy_ (u"ࠤࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴࠤᏇ") if self.bstack11l11ll11l_opy_() else bstack11111_opy_ (u"ࠥࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴࠤᏈ")
        self.bstack1l1l1ll11ll_opy_[bstack11111_opy_ (u"ࠦ࠿ࠨᏉ").join([tag + bstack11111_opy_ (u"ࠧ࠳ࠢᏊ") + str(id(self)), key])] += value
    def bstack111l1111ll_opy_(self):
        if not os.getenv(bstack11111_opy_ (u"ࠨࡄࡆࡄࡘࡋࡤࡖࡅࡓࡈࠥᏋ"), bstack11111_opy_ (u"ࠢ࠱ࠤᏌ")) == bstack11111_opy_ (u"ࠣ࠳ࠥᏍ"):
            return
        bstack1l1l111l1ll_opy_ = dict()
        bstack1lll1l1l1l1_opy_ = []
        if self.test_framework:
            bstack1lll1l1l1l1_opy_.extend(list(self.test_framework.bstack1lll1l1l1l1_opy_.values()))
        if self.bstack1llll1l1l11_opy_:
            bstack1lll1l1l1l1_opy_.extend(list(self.bstack1llll1l1l11_opy_.bstack1lll1l1l1l1_opy_.values()))
        for instance in bstack1lll1l1l1l1_opy_:
            if not instance.platform_index in bstack1l1l111l1ll_opy_:
                bstack1l1l111l1ll_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l111l1ll_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll11111_opy_().items():
                report[k] += v
                report[k.split(bstack11111_opy_ (u"ࠤ࠽ࠦᏎ"))[0]] += v
        bstack1l1l1l1ll1l_opy_ = sorted([(k, v) for k, v in self.bstack1l1l1ll11ll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l11l1l1l_opy_ = 0
        for r in bstack1l1l1l1ll1l_opy_:
            bstack1l1l1l1lll1_opy_ = r[1].total_seconds()
            bstack1l1l11l1l1l_opy_ += bstack1l1l1l1lll1_opy_
            self.logger.debug(bstack11111_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡧࡱ࡯࠺ࡼࡴ࡞࠴ࡢࢃ࠽ࠣᏏ") + str(bstack1l1l1l1lll1_opy_) + bstack11111_opy_ (u"ࠦࠧᏐ"))
        self.logger.debug(bstack11111_opy_ (u"ࠧ࠳࠭ࠣᏑ"))
        bstack1l11ll1111l_opy_ = []
        for platform_index, report in bstack1l1l111l1ll_opy_.items():
            bstack1l11ll1111l_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l11ll1111l_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll11111_opy_ = set()
        bstack1l1l111ll11_opy_ = 0
        for r in bstack1l11ll1111l_opy_:
            bstack1l1l1l1lll1_opy_ = r[2].total_seconds()
            bstack1l1l111ll11_opy_ += bstack1l1l1l1lll1_opy_
            bstack1lll11111_opy_.add(r[0])
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡴࡦࡵࡷ࠾ࡵࡲࡡࡵࡨࡲࡶࡲ࠳ࡻࡳ࡝࠳ࡡࢂࡀࡻࡳ࡝࠴ࡡࢂࡃࠢᏒ") + str(bstack1l1l1l1lll1_opy_) + bstack11111_opy_ (u"ࠢࠣᏓ"))
        if self.bstack11l11ll11l_opy_():
            self.logger.debug(bstack11111_opy_ (u"ࠣ࠯࠰ࠦᏔ"))
            self.logger.debug(bstack11111_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡃࡻࡵࡱࡷࡥࡱࡥࡣ࡭࡫ࢀࠤࡹ࡫ࡳࡵ࠼ࡳࡰࡦࡺࡦࡰࡴࡰࡷ࠲ࢁࡳࡵࡴࠫࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠯ࡽ࠾ࠤᏕ") + str(bstack1l1l111ll11_opy_) + bstack11111_opy_ (u"ࠥࠦᏖ"))
        else:
            self.logger.debug(bstack11111_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹ࠽ࠣᏗ") + str(bstack1l1l11l1l1l_opy_) + bstack11111_opy_ (u"ࠧࠨᏘ"))
        self.logger.debug(bstack11111_opy_ (u"ࠨ࠭࠮ࠤᏙ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1llll1ll1ll_opy_:
            self.logger.error(bstack11111_opy_ (u"ࠢࡤ࡮࡬ࡣࡸ࡫ࡲࡷ࡫ࡦࡩࠥ࡯ࡳࠡࡰࡲࡸࠥ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࡦ࠱ࠤࡈࡧ࡮࡯ࡱࡷࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦᏚ"))
            return None
        response = self.bstack1llll1ll1ll_opy_.TestOrchestration(request)
        self.logger.debug(bstack11111_opy_ (u"ࠣࡶࡨࡷࡹ࠳࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠳ࡳࡦࡵࡶ࡭ࡴࡴ࠽ࡼࡿࠥᏛ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l1ll1lll_opy_(self, r):
        if r is not None and getattr(r, bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࠪᏜ"), None) and getattr(r.testhub, bstack11111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪᏝ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᏞ")))
            for bstack1l11llll1l1_opy_, err in errors.items():
                if err[bstack11111_opy_ (u"ࠬࡺࡹࡱࡧࠪᏟ")] == bstack11111_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᏠ"):
                    self.logger.info(err[bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᏡ")])
                else:
                    self.logger.error(err[bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᏢ")])
    def bstack1lll1l11ll_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()