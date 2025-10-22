# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11l1l11_opy_ import bstack1lll11l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack1l11lllll11_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll111lll_opy_ import bstack1l1ll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1lll1l1_opy_ import bstack1l11ll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll111ll_opy_ import bstack1lllll1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1ll1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l11_opy_ import bstack1lll11l1lll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1l111l1_opy_ import bstack1l1l111llll_opy_
from browserstack_sdk.sdk_cli.bstack1l11l1lll_opy_ import bstack1l11l1lll_opy_, Events, bstack111lllllll_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1l1l1l1_opy_ import bstack1l1l1ll111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lll1111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1l1l1ll_opy_
from bstack_utils.helper import Notset, bstack1l11lll1ll1_opy_, get_cli_dir, bstack1l1l1l1lll1_opy_, bstack11l1ll11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1l1lll1lll1_opy_ import bstack1ll1111ll11_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11111l1_opy_ import bstack11l111l11l_opy_
from bstack_utils.helper import Notset, bstack1l11lll1ll1_opy_, get_cli_dir, bstack1l1l1l1lll1_opy_, bstack11l1ll11l1_opy_, bstack11l1l111l1_opy_, bstack1llllll111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1l1llll_opy_, bstack1lll1lll111_opy_, bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll111l1_opy_, bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1l11l1l111_opy_ import bstack1l111ll1l1_opy_
from bstack_utils import bstack11llll111l_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11l11l1l1l_opy_, bstack1l11lll11_opy_
logger = bstack11llll111l_opy_.get_logger(__name__, bstack11llll111l_opy_.bstack1l1l11l11ll_opy_())
def bstack1l1l11111l1_opy_(bs_config):
    bstack1l1l1l11lll_opy_ = None
    bstack1l1l1l11ll1_opy_ = None
    try:
        bstack1l1l1l11ll1_opy_ = get_cli_dir()
        bstack1l1l1l11lll_opy_ = bstack1l1l1l1lll1_opy_(bstack1l1l1l11ll1_opy_)
        bstack1l11lll1l11_opy_ = bstack1l11lll1ll1_opy_(bstack1l1l1l11lll_opy_, bstack1l1l1l11ll1_opy_, bs_config)
        bstack1l1l1l11lll_opy_ = bstack1l11lll1l11_opy_ if bstack1l11lll1l11_opy_ else bstack1l1l1l11lll_opy_
        if not bstack1l1l1l11lll_opy_:
            raise ValueError(bstack1lllll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠧጉ"))
    except Exception as ex:
        logger.debug(bstack1lllll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡺࡨࡦࠢ࡯ࡥࡹ࡫ࡳࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡾࢁࠧጊ").format(ex))
        bstack1l1l1l11lll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠨጋ"))
        if bstack1l1l1l11lll_opy_:
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠢࡩࡶࡴࡳࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸ࠿ࠦࠢጌ") + str(bstack1l1l1l11lll_opy_) + bstack1lllll1l_opy_ (u"ࠧࠨግ"))
        else:
            logger.debug(bstack1lllll1l_opy_ (u"ࠨࡎࡰࠢࡹࡥࡱ࡯ࡤࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷ࠿ࠥࡹࡥࡵࡷࡳࠤࡲࡧࡹࠡࡤࡨࠤ࡮ࡴࡣࡰ࡯ࡳࡰࡪࡺࡥ࠯ࠤጎ"))
    return bstack1l1l1l11lll_opy_, bstack1l1l1l11ll1_opy_
bstack1l1l1ll1l11_opy_ = bstack1lllll1l_opy_ (u"ࠢ࠺࠻࠼࠽ࠧጏ")
bstack1l1l1llllll_opy_ = bstack1lllll1l_opy_ (u"ࠣࡴࡨࡥࡩࡿࠢጐ")
bstack1l11lll1l1l_opy_ = bstack1lllll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡖࡉࡘ࡙ࡉࡐࡐࡢࡍࡉࠨ጑")
bstack1l1l1llll11_opy_ = bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡐࡎ࡙ࡔࡆࡐࡢࡅࡉࡊࡒࠣጒ")
bstack11ll1l1l1l_opy_ = bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠢጓ")
bstack1l1l1lll1ll_opy_ = re.compile(bstack1lllll1l_opy_ (u"ࡷࠨࠨࡀ࡫ࠬ࠲࠯࠮ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࢁࡈࡓࠪ࠰࠭ࠦጔ"))
bstack1l11ll1lll1_opy_ = bstack1lllll1l_opy_ (u"ࠨࡤࡦࡸࡨࡰࡴࡶ࡭ࡦࡰࡷࠦጕ")
bstack1l1l11ll1l1_opy_ = bstack1lllll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡐࡔࡆࡉࡤࡌࡁࡍࡎࡅࡅࡈࡑࠢ጖")
bstack1l1l1l1ll11_opy_ = [
    Events.bstack1111ll1111_opy_,
    Events.CONNECT,
    Events.bstack1lll1111ll_opy_,
]
class SDKCLI:
    _1ll1l1llll1_opy_ = None
    process: Union[None, Any]
    bstack1l1l1ll11ll_opy_: bool
    bstack1l11llll11l_opy_: bool
    bstack1l1l11l1l11_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1ll111111_opy_: Union[None, grpc.Channel]
    bstack1l1l111l1ll_opy_: str
    test_framework: TestFramework
    bstack1llll1ll111_opy_: bstack1lll1111l1l_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l11lll1l_opy_: bstack1l1l111llll_opy_
    accessibility: bstack1l11lllll11_opy_
    bstack1ll11111l1_opy_: bstack11l111l11l_opy_
    ai: bstack1l1ll11lll1_opy_
    bstack1l11llll111_opy_: bstack1l11ll11lll_opy_
    bstack1l1l1111l11_opy_: List[bstack1lllll1111l_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l111ll11_opy_: Any
    bstack1l11lll1lll_opy_: Dict[str, timedelta]
    bstack1l1l1llll1l_opy_: str
    bstack1lll11l1l11_opy_: bstack1lll11l1l1l_opy_
    def __new__(cls):
        if not cls._1ll1l1llll1_opy_:
            cls._1ll1l1llll1_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1l1llll1_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1l1ll11ll_opy_ = False
        self.bstack1l1ll111111_opy_ = None
        self.bstack1lllllll111_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l1llll11_opy_, None)
        self.bstack1l11ll1ll11_opy_ = os.environ.get(bstack1l11lll1l1l_opy_, bstack1lllll1l_opy_ (u"ࠣࠤ጗")) == bstack1lllll1l_opy_ (u"ࠤࠥጘ")
        self.bstack1l11llll11l_opy_ = False
        self.bstack1l1l11l1l11_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l111ll11_opy_ = None
        self.test_framework = None
        self.bstack1llll1ll111_opy_ = None
        self.bstack1l1l111l1ll_opy_=bstack1lllll1l_opy_ (u"ࠥࠦጙ")
        self.session_framework = None
        self.logger = bstack11llll111l_opy_.get_logger(self.__class__.__name__, bstack11llll111l_opy_.bstack1l1l11l11ll_opy_())
        self.bstack1l11lll1lll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11l1l11_opy_ = bstack1lll11l1l1l_opy_()
        self.bstack1l11ll1l1ll_opy_ = None
        self.bstack1ll1ll1l111_opy_ = None
        self.bstack1l1l11lll1l_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l1111l11_opy_ = []
    def bstack111l1lll11_opy_(self):
        return os.environ.get(bstack11ll1l1l1l_opy_).lower().__eq__(bstack1lllll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤጚ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l11ll1l1_opy_, bstack1lllll1l_opy_ (u"ࠬ࠭ጛ")).lower() in [bstack1lllll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫጜ"), bstack1lllll1l_opy_ (u"ࠧ࠲ࠩጝ"), bstack1lllll1l_opy_ (u"ࠨࡻࡨࡷࠬጞ")]:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡉࡳࡷࡩࡩ࡯ࡩࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡳ࡯ࡥࡧࠣࡨࡺ࡫ࠠࡵࡱࠣࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡓࡗࡉࡅࡠࡈࡄࡐࡑࡈࡁࡄࡍࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴࠡࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠥጟ"))
            os.environ[bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨጠ")] = bstack1lllll1l_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥጡ")
            return False
        if bstack1lllll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩጢ") in config and str(config[bstack1lllll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪጣ")]).lower() != bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ጤ"):
            return False
        bstack1l1l11lll11_opy_ = [bstack1lllll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣጥ"), bstack1lllll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨጦ")]
        bstack1l1l11111ll_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨጧ")) in bstack1l1l11lll11_opy_ or os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬጨ")) in bstack1l1l11lll11_opy_
        os.environ[bstack1lllll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣጩ")] = str(bstack1l1l11111ll_opy_) # bstack1l1l11ll11l_opy_ bstack1l11lll1111_opy_ VAR to bstack1l1l11llll1_opy_ is binary running
        return bstack1l1l11111ll_opy_
    def bstack1111lll1l1_opy_(self):
        for event in bstack1l1l1l1ll11_opy_:
            bstack1l11l1lll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l11l1lll_opy_.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠥࡃ࠾ࠡࡽࡤࡶ࡬ࡹࡽࠡࠤጪ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠢࠣጫ"))
            )
        bstack1l11l1lll_opy_.register(Events.bstack1111ll1111_opy_, self.__1l1l1ll11l1_opy_)
        bstack1l11l1lll_opy_.register(Events.CONNECT, self.__1l1l1l11l1l_opy_)
        bstack1l11l1lll_opy_.register(Events.bstack1lll1111ll_opy_, self.__1l1l111111l_opy_)
        bstack1l11l1lll_opy_.register(Events.bstack1l111111ll_opy_, self.__1l1l111l111_opy_)
    def bstack11111l1l1_opy_(self):
        return not self.bstack1l11ll1ll11_opy_ and os.environ.get(bstack1l11lll1l1l_opy_, bstack1lllll1l_opy_ (u"ࠣࠤጬ")) != bstack1lllll1l_opy_ (u"ࠤࠥጭ")
    def is_running(self):
        if self.bstack1l11ll1ll11_opy_:
            return self.bstack1l1l1ll11ll_opy_
        else:
            return bool(self.bstack1l1ll111111_opy_)
    def bstack1l11llll1l1_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l1111l11_opy_) and cli.is_running()
    def __1l1l1lll111_opy_(self, bstack1l1l111lll1_opy_=10):
        if self.bstack1lllllll111_opy_:
            return
        bstack1ll111ll1_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l1llll11_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠥ࡟ࠧጮ") + str(id(self)) + bstack1lllll1l_opy_ (u"ࠦࡢࠦࡣࡰࡰࡱࡩࡨࡺࡩ࡯ࡩࠥጯ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1lllll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠱ࡩࡳࡧࡢ࡭ࡧࡢ࡬ࡹࡺࡰࡠࡲࡵࡳࡽࡿࠢጰ"), 0), (bstack1lllll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠲ࡪࡴࡡࡣ࡮ࡨࡣ࡭ࡺࡴࡱࡵࡢࡴࡷࡵࡸࡺࠤጱ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l111lll1_opy_)
        self.bstack1l1ll111111_opy_ = channel
        self.bstack1lllllll111_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1ll111111_opy_)
        self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡩ࡯࡯ࡰࡨࡧࡹࠨጲ"), datetime.now() - bstack1ll111ll1_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l1llll11_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦ࠽ࠤ࡮ࡹ࡟ࡤࡪ࡬ࡰࡩࡥࡰࡳࡱࡦࡩࡸࡹ࠽ࠣጳ") + str(self.bstack11111l1l1_opy_()) + bstack1lllll1l_opy_ (u"ࠤࠥጴ"))
    def __1l1l111111l_opy_(self, event_name):
        if self.bstack11111l1l1_opy_():
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡸࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡃࡍࡋࠥጵ"))
        self.__1l11lll111l_opy_()
    def __1l1l111l111_opy_(self, event_name, bstack1l11ll1ll1l_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠦጶ"))
        bstack1l11ll1l111_opy_ = Path(bstack11ll1l1l_opy_ (u"ࠧࢁࡳࡦ࡮ࡩ࠲ࡨࡲࡩࡠࡦ࡬ࡶࢂ࠵ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࡳ࠯࡬ࡶࡳࡳࠨጷ"))
        if self.bstack1l1l1l11ll1_opy_ and bstack1l11ll1l111_opy_.exists():
            with open(bstack1l11ll1l111_opy_, bstack1lllll1l_opy_ (u"࠭ࡲࠨጸ"), encoding=bstack1lllll1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ጹ")) as fp:
                data = json.load(fp)
                try:
                    bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭ጺ"), bstack1l111ll1l1_opy_(bstack111l1l11l1_opy_), data, {
                        bstack1lllll1l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧጻ"): (self.config[bstack1lllll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬጼ")], self.config[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧጽ")])
                    })
                except Exception as e:
                    logger.debug(bstack1l11lll11_opy_.format(str(e)))
            bstack1l11ll1l111_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l111ll1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1l1l1ll11l1_opy_(self, event_name: str, data):
        from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
        self.bstack1l1l111l1ll_opy_, self.bstack1l1l1l11ll1_opy_ = bstack1l1l11111l1_opy_(data.bs_config)
        os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡜ࡘࡉࡕࡃࡅࡐࡊࡥࡄࡊࡔࠪጾ")] = self.bstack1l1l1l11ll1_opy_
        if not self.bstack1l1l111l1ll_opy_ or not self.bstack1l1l1l11ll1_opy_:
            raise ValueError(bstack1lllll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡵࡪࡨࠤࡘࡊࡋࠡࡅࡏࡍࠥࡨࡩ࡯ࡣࡵࡽࠧጿ"))
        if self.bstack11111l1l1_opy_():
            self.__1l1l1l11l1l_opy_(event_name, bstack111lllllll_opy_())
            return
        try:
            bstack1llllllll1l_opy_.end(EVENTS.bstack1l111llll_opy_.value, EVENTS.bstack1l111llll_opy_.value + bstack1lllll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢፀ"), EVENTS.bstack1l111llll_opy_.value + bstack1lllll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨፁ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1lllll1l_opy_ (u"ࠤࡆࡳࡲࡶ࡬ࡦࡶࡨࠤࡘࡊࡋࠡࡕࡨࡸࡺࡶ࠮ࠣፂ"))
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࢀࢃࠢፃ").format(e))
        start = datetime.now()
        is_started = self.__1l1l11l11l1_opy_()
        self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦࡸࡶࡡࡸࡰࡢࡸ࡮ࡳࡥࠣፄ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l1lll111_opy_()
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࡥࡴࡪ࡯ࡨࠦፅ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1l1l1l1ll_opy_(data)
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦፆ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l11ll111ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1l1l1l11l1l_opy_(self, event_name: str, data: bstack111lllllll_opy_):
        if not self.bstack11111l1l1_opy_():
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡴ࡮ࡦࡥࡷ࠾ࠥࡴ࡯ࡵࠢࡤࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦፇ"))
            return
        bin_session_id = os.environ.get(bstack1l11lll1l1l_opy_)
        start = datetime.now()
        self.__1l1l1lll111_opy_()
        self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢፈ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠥࡺ࡯ࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡇࡑࡏࠠࠣፉ") + str(bin_session_id) + bstack1lllll1l_opy_ (u"ࠥࠦፊ"))
        start = datetime.now()
        self.__1l1l1l11l11_opy_()
        self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤፋ"), datetime.now() - start)
    def __1l1l11l1111_opy_(self):
        if not self.bstack1lllllll111_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࠡ࡯ࡲࡨࡺࡲࡥࡴࠤፌ"))
            return
        bstack1l1ll111l11_opy_ = {
            bstack1lllll1l_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥፍ"): (bstack1ll1ll1l1ll_opy_, bstack1lll11l1lll_opy_, bstack1lll1l1l1ll_opy_),
            bstack1lllll1l_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤፎ"): (bstack1lllll1l1ll_opy_, bstack1lll11l11l1_opy_, bstack1llll1lllll_opy_),
        }
        if not self.bstack1l11ll1l1ll_opy_ and self.session_framework in bstack1l1ll111l11_opy_:
            bstack1l1l1111111_opy_, bstack1l11lll11ll_opy_, bstack1l1l1l1111l_opy_ = bstack1l1ll111l11_opy_[self.session_framework]
            bstack1l1l1lll11l_opy_ = bstack1l11lll11ll_opy_()
            self.bstack1ll1ll1l111_opy_ = bstack1l1l1lll11l_opy_
            self.bstack1l11ll1l1ll_opy_ = bstack1l1l1l1111l_opy_
            self.bstack1l1l1111l11_opy_.append(bstack1l1l1lll11l_opy_)
            self.bstack1l1l1111l11_opy_.append(bstack1l1l1111111_opy_(self.bstack1ll1ll1l111_opy_))
        if not self.bstack1l1l11lll1l_opy_ and self.config_observability and self.config_observability.success: # bstack1lllll11ll1_opy_
            self.bstack1l1l11lll1l_opy_ = bstack1l1l111llll_opy_(self.bstack1l11ll1l1ll_opy_, self.bstack1ll1ll1l111_opy_) # bstack1l1l1ll1l1l_opy_
            self.bstack1l1l1111l11_opy_.append(self.bstack1l1l11lll1l_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l11lllll11_opy_(self.bstack1l11ll1l1ll_opy_, self.bstack1ll1ll1l111_opy_)
            self.bstack1l1l1111l11_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1lllll1l_opy_ (u"ࠣࡵࡨࡰ࡫ࡎࡥࡢ࡮ࠥፏ"), False) == True:
            self.ai = bstack1l1ll11lll1_opy_()
            self.bstack1l1l1111l11_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l111ll11_opy_ and self.bstack1l1l111ll11_opy_.success:
            self.percy = bstack1l11ll11lll_opy_(self.bstack1l1l111ll11_opy_)
            self.bstack1l1l1111l11_opy_.append(self.percy)
        for mod in self.bstack1l1l1111l11_opy_:
            if not mod.bstack1lll11l1ll1_opy_():
                mod.configure(self.bstack1lllllll111_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11l1l11_opy_)
    def __1l1l1111lll_opy_(self):
        for mod in self.bstack1l1l1111l11_opy_:
            if mod.bstack1lll11l1ll1_opy_():
                mod.configure(self.bstack1lllllll111_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l1l1l1l11l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1l1l1l1l1ll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l11llll11l_opy_:
            return
        self.__1l11ll11l1l_opy_(data)
        bstack1ll111ll1_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1lllll1l_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤፐ")
        req.sdk_language = bstack1lllll1l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥፑ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l1lll1ll_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡠࠨፒ") + str(id(self)) + bstack1lllll1l_opy_ (u"ࠧࡣࠠ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦፓ"))
            r = self.bstack1lllllll111_opy_.StartBinSession(req)
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺࡡࡳࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣፔ"), datetime.now() - bstack1ll111ll1_opy_)
            os.environ[bstack1l11lll1l1l_opy_] = r.bin_session_id
            self.__1l1l11ll1ll_opy_(r)
            self.__1l1l11l1111_opy_()
            self.bstack1lll11l1l11_opy_.start()
            self.bstack1l11llll11l_opy_ = True
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢ࡜ࠤፕ") + str(id(self)) + bstack1lllll1l_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠨፖ"))
        except grpc.bstack1l1l11l111l_opy_ as bstack1l11llllll1_opy_:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦፗ") + str(bstack1l11llllll1_opy_) + bstack1lllll1l_opy_ (u"ࠥࠦፘ"))
            traceback.print_exc()
            raise bstack1l11llllll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣፙ") + str(e) + bstack1lllll1l_opy_ (u"ࠧࠨፚ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11ll11ll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1l1l1l11l11_opy_(self):
        if not self.bstack11111l1l1_opy_() or not self.cli_bin_session_id or self.bstack1l1l11l1l11_opy_:
            return
        bstack1ll111ll1_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭፛"), bstack1lllll1l_opy_ (u"ࠧ࠱ࠩ፜")))
        try:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡝ࠥ፝") + str(id(self)) + bstack1lllll1l_opy_ (u"ࠤࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦ፞"))
            r = self.bstack1lllllll111_opy_.ConnectBinSession(req)
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢ፟"), datetime.now() - bstack1ll111ll1_opy_)
            self.__1l1l11ll1ll_opy_(r)
            self.__1l1l11l1111_opy_()
            self.bstack1lll11l1l11_opy_.start()
            self.bstack1l1l11l1l11_opy_ = True
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡠࠨ፠") + str(id(self)) + bstack1lllll1l_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠦ፡"))
        except grpc.bstack1l1l11l111l_opy_ as bstack1l11llllll1_opy_:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡺࡩ࡮ࡧࡲࡩࡺࡺ࠭ࡦࡴࡵࡳࡷࡀࠠࠣ።") + str(bstack1l11llllll1_opy_) + bstack1lllll1l_opy_ (u"ࠢࠣ፣"))
            traceback.print_exc()
            raise bstack1l11llllll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ፤") + str(e) + bstack1lllll1l_opy_ (u"ࠤࠥ፥"))
            traceback.print_exc()
            raise e
    def __1l1l11ll1ll_opy_(self, r):
        self.bstack1l1l111l11l_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1lllll1l_opy_ (u"ࠥࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡴࡧࡵࡺࡪࡸࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤ፦") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1lllll1l_opy_ (u"ࠦࡪࡳࡰࡵࡻࠣࡧࡴࡴࡦࡪࡩࠣࡪࡴࡻ࡮ࡥࠤ፧"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1lllll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡩࡷࡩࡹࠡ࡫ࡶࠤࡸ࡫࡮ࡵࠢࡲࡲࡱࡿࠠࡢࡵࠣࡴࡦࡸࡴࠡࡱࡩࠤࡹ࡮ࡥࠡࠤࡆࡳࡳࡴࡥࡤࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠲ࠢࠡࡣࡱࡨࠥࡺࡨࡪࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡣ࡯ࡷࡴࠦࡵࡴࡧࡧࠤࡧࡿࠠࡔࡶࡤࡶࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࡳࡧࡩࡳࡷ࡫ࠬࠡࡐࡲࡲࡪࠦࡨࡢࡰࡧࡰ࡮ࡴࡧࠡ࡫ࡶࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ፨")
        self.bstack1l1l111ll11_opy_ = getattr(r, bstack1lllll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ፩"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ፪")] = self.config_testhub.jwt
        os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭፫")] = self.config_testhub.build_hashed_id
    def bstack1l1l1l1l111_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1l1ll11ll_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l11lllll1l_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l11lllll1l_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1l1l1l111_opy_(event_name=EVENTS.bstack1l11ll1l11l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1l1l11l11l1_opy_(self, bstack1l1l111lll1_opy_=10):
        if self.bstack1l1l1ll11ll_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡶࡸࡦࡸࡴ࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡶࡺࡴ࡮ࡪࡰࡪࠦ፬"))
            return True
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡷࡹࡧࡲࡵࠤ፭"))
        if os.getenv(bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡆࡐ࡙ࠦ፮")) == bstack1l11ll1lll1_opy_:
            self.cli_bin_session_id = bstack1l11ll1lll1_opy_
            self.cli_listen_addr = bstack1lllll1l_opy_ (u"ࠧࡻ࡮ࡪࡺ࠽࠳ࡹࡳࡰ࠰ࡵࡧ࡯࠲ࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࠦࡵ࠱ࡷࡴࡩ࡫ࠣ፯") % (self.cli_bin_session_id)
            self.bstack1l1l1ll11ll_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l111l1ll_opy_, bstack1lllll1l_opy_ (u"ࠨࡳࡥ࡭ࠥ፰")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l11ll1l1l1_opy_ compat for text=True in bstack1l1ll1111l1_opy_ python
            encoding=bstack1lllll1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨ፱"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1ll11111l_opy_ = threading.Thread(target=self.__1l1l11l1l1l_opy_, args=(bstack1l1l111lll1_opy_,))
        bstack1l1ll11111l_opy_.start()
        bstack1l1ll11111l_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡴࡲࡤࡻࡳࡀࠠࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࡁࢀࡹࡥ࡭ࡨ࠱ࡴࡷࡵࡣࡦࡵࡶ࠲ࡷ࡫ࡴࡶࡴࡱࡧࡴࡪࡥࡾࠢࡲࡹࡹࡃࡻࡴࡧ࡯ࡪ࠳ࡶࡲࡰࡥࡨࡷࡸ࠴ࡳࡵࡦࡲࡹࡹ࠴ࡲࡦࡣࡧࠬ࠮ࢃࠠࡦࡴࡵࡁࠧ፲") + str(self.process.stderr.read()) + bstack1lllll1l_opy_ (u"ࠤࠥ፳"))
        if not self.bstack1l1l1ll11ll_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥ࡟ࠧ፴") + str(id(self)) + bstack1lllll1l_opy_ (u"ࠦࡢࠦࡣ࡭ࡧࡤࡲࡺࡶࠢ፵"))
            self.__1l11lll111l_opy_()
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡵࡸ࡯ࡤࡧࡶࡷࡤࡸࡥࡢࡦࡼ࠾ࠥࠨ፶") + str(self.bstack1l1l1ll11ll_opy_) + bstack1lllll1l_opy_ (u"ࠨࠢ፷"))
        return self.bstack1l1l1ll11ll_opy_
    def __1l1l11l1l1l_opy_(self, bstack1l1l1ll1ll1_opy_=10):
        bstack1l1l1lllll1_opy_ = time.time()
        while self.process and time.time() - bstack1l1l1lllll1_opy_ < bstack1l1l1ll1ll1_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1lllll1l_opy_ (u"ࠢࡪࡦࡀࠦ፸") in line:
                    self.cli_bin_session_id = line.split(bstack1lllll1l_opy_ (u"ࠣ࡫ࡧࡁࠧ፹"))[-1:][0].strip()
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡦࡰ࡮ࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠺ࠣ፺") + str(self.cli_bin_session_id) + bstack1lllll1l_opy_ (u"ࠥࠦ፻"))
                    continue
                if bstack1lllll1l_opy_ (u"ࠦࡱ࡯ࡳࡵࡧࡱࡁࠧ፼") in line:
                    self.cli_listen_addr = line.split(bstack1lllll1l_opy_ (u"ࠧࡲࡩࡴࡶࡨࡲࡂࠨ፽"))[-1:][0].strip()
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡣ࡭࡫ࡢࡰ࡮ࡹࡴࡦࡰࡢࡥࡩࡪࡲ࠻ࠤ፾") + str(self.cli_listen_addr) + bstack1lllll1l_opy_ (u"ࠢࠣ፿"))
                    continue
                if bstack1lllll1l_opy_ (u"ࠣࡲࡲࡶࡹࡃࠢᎀ") in line:
                    port = line.split(bstack1lllll1l_opy_ (u"ࠤࡳࡳࡷࡺ࠽ࠣᎁ"))[-1:][0].strip()
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡴࡴࡸࡴ࠻ࠤᎂ") + str(port) + bstack1lllll1l_opy_ (u"ࠦࠧᎃ"))
                    continue
                if line.strip() == bstack1l1l1llllll_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1lllll1l_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡎࡕ࡟ࡔࡖࡕࡉࡆࡓࠢᎄ"), bstack1lllll1l_opy_ (u"ࠨ࠱ࠣᎅ")) == bstack1lllll1l_opy_ (u"ࠢ࠲ࠤᎆ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1l1ll11ll_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡧࡵࡶࡴࡸ࠺ࠡࠤᎇ") + str(e) + bstack1lllll1l_opy_ (u"ࠤࠥᎈ"))
        return False
    @measure(event_name=EVENTS.bstack1l11ll11l11_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1l11lll111l_opy_(self):
        if self.bstack1l1ll111111_opy_:
            self.bstack1lll11l1l11_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l1l11111_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l11l1l11_opy_:
                    self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠥࡷࡹࡵࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢᎉ"), datetime.now() - start)
                else:
                    self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦࡸࡺ࡯ࡱࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣᎊ"), datetime.now() - start)
            self.__1l1l1111lll_opy_()
            start = datetime.now()
            self.bstack1l1ll111111_opy_.close()
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠧࡪࡩࡴࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢᎋ"), datetime.now() - start)
            self.bstack1l1ll111111_opy_ = None
        if self.process:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡳࡵࡱࡳࠦᎌ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠢ࡬࡫࡯ࡰࡤࡺࡩ࡮ࡧࠥᎍ"), datetime.now() - start)
            self.process = None
            if self.bstack1l11ll1ll11_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack11ll1ll1ll_opy_()
                self.logger.info(
                    bstack1lllll1l_opy_ (u"ࠣࡘ࡬ࡷ࡮ࡺࠠࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠣᎎ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᎏ")] = self.config_testhub.build_hashed_id
        self.bstack1l1l1ll11ll_opy_ = False
    def __1l11ll11l1l_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1lllll1l_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ᎐")] = selenium.__version__
            data.frameworks.append(bstack1lllll1l_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ᎑"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1lllll1l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ᎒")] = __version__
            data.frameworks.append(bstack1lllll1l_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ᎓"))
        except:
            pass
    def bstack1l1l1l1ll1l_opy_(self, hub_url: str, platform_index: int, bstack1l1l11l111_opy_: Any):
        if self.bstack1llll1ll111_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡸ࡫ࡴࠡࡷࡳࠦ᎔"))
            return
        try:
            bstack1ll111ll1_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1lllll1l_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ᎕")
            self.bstack1llll1ll111_opy_ = bstack1llll1lllll_opy_(
                cli.config.get(bstack1lllll1l_opy_ (u"ࠤ࡫ࡹࡧ࡛ࡲ࡭ࠤ᎖"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll1ll11l_opy_={bstack1lllll1l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡢࡳࡵࡺࡩࡰࡰࡶࡣ࡫ࡸ࡯࡮ࡡࡦࡥࡵࡹࠢ᎗"): bstack1l1l11l111_opy_}
            )
            def bstack1l1l1ll1111_opy_(self):
                return
            if self.config.get(bstack1lllll1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠨ᎘"), True):
                Service.start = bstack1l1l1ll1111_opy_
                Service.stop = bstack1l1l1ll1111_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack11l111l11l_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll1111ll11_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ᎙"), datetime.now() - bstack1ll111ll1_opy_)
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡵࡨࡰࡪࡴࡩࡶ࡯࠽ࠤࠧ᎚") + str(e) + bstack1lllll1l_opy_ (u"ࠢࠣ᎛"))
    def bstack1l1l111l1l1_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack111l111ll_opy_
            self.bstack1llll1ll111_opy_ = bstack1lll1l1l1ll_opy_(
                platform_index,
                framework_name=bstack1lllll1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ᎜"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠻ࠢࠥ᎝") + str(e) + bstack1lllll1l_opy_ (u"ࠥࠦ᎞"))
            pass
    def bstack1l1l1111l1l_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡳࡦࡶࠣࡹࡵࠨ᎟"))
            return
        if bstack11l1ll11l1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1lllll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᎠ"): pytest.__version__ }, [bstack1lllll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᎡ")], self.bstack1lll11l1l11_opy_, self.bstack1lllllll111_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l1l1ll111l_opy_({ bstack1lllll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᎢ"): pytest.__version__ }, [bstack1lllll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᎣ")], self.bstack1lll11l1l11_opy_, self.bstack1lllllll111_opy_)
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵࡿࡴࡦࡵࡷ࠾ࠥࠨᎤ") + str(e) + bstack1lllll1l_opy_ (u"ࠥࠦᎥ"))
        self.bstack1l1l1l1llll_opy_()
    def bstack1l1l1l1llll_opy_(self):
        if not self.bstack111l1lll11_opy_():
            return
        bstack11111l1lll_opy_ = None
        def bstack1l11111l1l_opy_(config, startdir):
            return bstack1lllll1l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤᎦ").format(bstack1lllll1l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦᎧ"))
        def bstack1l1ll1ll1l_opy_():
            return
        def bstack11l1ll111_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1lllll1l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭Ꭸ"):
                return bstack1lllll1l_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨᎩ")
            else:
                return bstack11111l1lll_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack11111l1lll_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1l11111l1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1ll1ll1l_opy_
            Config.getoption = bstack11l1ll111_opy_
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡴࡤࡪࠣࡴࡾࡺࡥࡴࡶࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࡬࡯ࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠻ࠢࠥᎪ") + str(e) + bstack1lllll1l_opy_ (u"ࠤࠥᎫ"))
    def bstack1l1l11l1lll_opy_(self):
        bstack1lll11l111_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1lll11l111_opy_, dict):
            if cli.config_observability:
                bstack1lll11l111_opy_.update(
                    {bstack1lllll1l_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥᎬ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1lllll1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢᎭ") in accessibility.get(bstack1lllll1l_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᎮ"), {}):
                    bstack1l1l1l111ll_opy_ = accessibility.get(bstack1lllll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᎯ"))
                    bstack1l1l1l111ll_opy_.update({ bstack1lllll1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠣᎰ"): bstack1l1l1l111ll_opy_.pop(bstack1lllll1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡢࡸࡴࡥࡷࡳࡣࡳࠦᎱ")) })
                bstack1lll11l111_opy_.update({bstack1lllll1l_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᎲ"): accessibility })
        return bstack1lll11l111_opy_
    @measure(event_name=EVENTS.bstack1l1l1111ll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1l1l1l11111_opy_(self, bstack1l1l11l1ll1_opy_: str = None, bstack1l11ll1llll_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1lllllll111_opy_:
            return
        bstack1ll111ll1_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l11l1ll1_opy_:
            req.bstack1l1l11l1ll1_opy_ = bstack1l1l11l1ll1_opy_
        if bstack1l11ll1llll_opy_:
            req.bstack1l11ll1llll_opy_ = bstack1l11ll1llll_opy_
        try:
            r = self.bstack1lllllll111_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡷࡳࡵࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦᎳ"), datetime.now() - bstack1ll111ll1_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1lll11llll_opy_(self, key: str, value: timedelta):
        tag = bstack1lllll1l_opy_ (u"ࠦࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᎴ") if self.bstack11111l1l1_opy_() else bstack1lllll1l_opy_ (u"ࠧࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶࠦᎵ")
        self.bstack1l11lll1lll_opy_[bstack1lllll1l_opy_ (u"ࠨ࠺ࠣᎶ").join([tag + bstack1lllll1l_opy_ (u"ࠢ࠮ࠤᎷ") + str(id(self)), key])] += value
    def bstack11ll1ll1ll_opy_(self):
        if not os.getenv(bstack1lllll1l_opy_ (u"ࠣࡆࡈࡆ࡚ࡍ࡟ࡑࡇࡕࡊࠧᎸ"), bstack1lllll1l_opy_ (u"ࠤ࠳ࠦᎹ")) == bstack1lllll1l_opy_ (u"ࠥ࠵ࠧᎺ"):
            return
        bstack1l1l1ll1lll_opy_ = dict()
        bstack1lll11lllll_opy_ = []
        if self.test_framework:
            bstack1lll11lllll_opy_.extend(list(self.test_framework.bstack1lll11lllll_opy_.values()))
        if self.bstack1llll1ll111_opy_:
            bstack1lll11lllll_opy_.extend(list(self.bstack1llll1ll111_opy_.bstack1lll11lllll_opy_.values()))
        for instance in bstack1lll11lllll_opy_:
            if not instance.platform_index in bstack1l1l1ll1lll_opy_:
                bstack1l1l1ll1lll_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l1ll1lll_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll11lll_opy_().items():
                report[k] += v
                report[k.split(bstack1lllll1l_opy_ (u"ࠦ࠿ࠨᎻ"))[0]] += v
        bstack1l11lllllll_opy_ = sorted([(k, v) for k, v in self.bstack1l11lll1lll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l11llll1ll_opy_ = 0
        for r in bstack1l11lllllll_opy_:
            bstack1l1ll1111ll_opy_ = r[1].total_seconds()
            bstack1l11llll1ll_opy_ += bstack1l1ll1111ll_opy_
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡾࡶࡠ࠶࡝ࡾ࠿ࠥᎼ") + str(bstack1l1ll1111ll_opy_) + bstack1lllll1l_opy_ (u"ࠨࠢᎽ"))
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠢ࠮࠯ࠥᎾ"))
        bstack1l1l11lllll_opy_ = []
        for platform_index, report in bstack1l1l1ll1lll_opy_.items():
            bstack1l1l11lllll_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l11lllll_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll1111l_opy_ = set()
        bstack1l1l11ll111_opy_ = 0
        for r in bstack1l1l11lllll_opy_:
            bstack1l1ll1111ll_opy_ = r[2].total_seconds()
            bstack1l1l11ll111_opy_ += bstack1l1ll1111ll_opy_
            bstack1lll1111l_opy_.add(r[0])
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡶࡨࡷࡹࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭࠮ࡽࡵ࡟࠵ࡣࡽ࠻ࡽࡵ࡟࠶ࡣࡽ࠾ࠤᎿ") + str(bstack1l1ll1111ll_opy_) + bstack1lllll1l_opy_ (u"ࠤࠥᏀ"))
        if self.bstack11111l1l1_opy_():
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥ࠱࠲ࠨᏁ"))
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻ࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠾ࡽࡷࡳࡹࡧ࡬ࡠࡥ࡯࡭ࢂࠦࡴࡦࡵࡷ࠾ࡵࡲࡡࡵࡨࡲࡶࡲࡹ࠭ࡼࡵࡷࡶ࠭ࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠪࡿࡀࠦᏂ") + str(bstack1l1l11ll111_opy_) + bstack1lllll1l_opy_ (u"ࠧࠨᏃ"))
        else:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠿ࠥᏄ") + str(bstack1l11llll1ll_opy_) + bstack1lllll1l_opy_ (u"ࠢࠣᏅ"))
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࠯࠰ࠦᏆ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1lllllll111_opy_:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡦࡰ࡮ࡥࡳࡦࡴࡹ࡭ࡨ࡫ࠠࡪࡵࠣࡲࡴࡺࠠࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࡨ࠳ࠦࡃࡢࡰࡱࡳࡹࠦࡰࡦࡴࡩࡳࡷࡳࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨᏇ"))
            return None
        response = self.bstack1lllllll111_opy_.TestOrchestration(request)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡸࡪࡹࡴ࠮ࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠮ࡵࡨࡷࡸ࡯࡯࡯࠿ࡾࢁࠧᏈ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l111l11l_opy_(self, r):
        if r is not None and getattr(r, bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࠬᏉ"), None) and getattr(r.testhub, bstack1lllll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬᏊ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1lllll1l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᏋ")))
            for bstack1l11lll11l1_opy_, err in errors.items():
                if err[bstack1lllll1l_opy_ (u"ࠧࡵࡻࡳࡩࠬᏌ")] == bstack1lllll1l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭Ꮝ"):
                    self.logger.info(err[bstack1lllll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᏎ")])
                else:
                    self.logger.error(err[bstack1lllll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᏏ")])
    def bstack11l1l1l111_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()