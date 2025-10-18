# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11lll1l_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1l1ll11ll11_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll1l1lll_opy_ import bstack1l1ll1l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1l1ll11_opy_ import bstack1l1l11111ll_opy_
from browserstack_sdk.sdk_cli.bstack11111111l1_opy_ import bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll111l11l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l11_opy_ import bstack1ll1lll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lll1l1l11l_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111l1l1_opy_ import bstack1l1l1l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll111ll_opy_ import bstack1llll111ll_opy_, Events, bstack1lll1l1l1l_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1l1llll_opy_ import bstack1l11lll1111_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import bstack1lll111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll1l11ll1_opy_
from bstack_utils.helper import Notset, bstack1l1ll11l111_opy_, get_cli_dir, bstack1l11ll1ll11_opy_, bstack1l1l1lll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll11l1l111_opy_ import bstack1ll1111ll1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1lll11_opy_ import bstack11l1llll11_opy_
from bstack_utils.helper import Notset, bstack1l1ll11l111_opy_, get_cli_dir, bstack1l11ll1ll11_opy_, bstack1l1l1lll1_opy_, bstack1l1l1l1l1l_opy_, bstack1l11l1l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11ll_opy_, bstack1lll1llll11_opy_, bstack1lll1lll11l_opy_, bstack1ll11ll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import bstack1llllllll1l_opy_, bstack1llll1lll11_opy_, bstack1llll1ll111_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1l1111llll_opy_ import bstack1l111l11l_opy_
from bstack_utils import bstack111l11l1l_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l1l111111_opy_, bstack111l1111l_opy_
logger = bstack111l11l1l_opy_.get_logger(__name__, bstack111l11l1l_opy_.bstack1l11lllll1l_opy_())
def bstack1l1l1l11l1l_opy_(bs_config):
    bstack1l1l1l1111l_opy_ = None
    bstack1l1l11lll11_opy_ = None
    try:
        bstack1l1l11lll11_opy_ = get_cli_dir()
        bstack1l1l1l1111l_opy_ = bstack1l11ll1ll11_opy_(bstack1l1l11lll11_opy_)
        bstack1l1ll1111l1_opy_ = bstack1l1ll11l111_opy_(bstack1l1l1l1111l_opy_, bstack1l1l11lll11_opy_, bs_config)
        bstack1l1l1l1111l_opy_ = bstack1l1ll1111l1_opy_ if bstack1l1ll1111l1_opy_ else bstack1l1l1l1111l_opy_
        if not bstack1l1l1l1111l_opy_:
            raise ValueError(bstack1l1lll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠥዤ"))
    except Exception as ex:
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡭ࡣࡷࡩࡸࡺࠠࡣ࡫ࡱࡥࡷࡿࠠࡼࡿࠥዥ").format(ex))
        bstack1l1l1l1111l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠦዦ"))
        if bstack1l1l1l1111l_opy_:
            logger.debug(bstack1l1lll1_opy_ (u"ࠤࡉࡥࡱࡲࡩ࡯ࡩࠣࡦࡦࡩ࡫ࠡࡶࡲࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠠࡧࡴࡲࡱࠥ࡫࡮ࡷ࡫ࡵࡳࡳࡳࡥ࡯ࡶ࠽ࠤࠧዧ") + str(bstack1l1l1l1111l_opy_) + bstack1l1lll1_opy_ (u"ࠥࠦየ"))
        else:
            logger.debug(bstack1l1lll1_opy_ (u"ࠦࡓࡵࠠࡷࡣ࡯࡭ࡩࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࡪࡴࡶࡪࡴࡲࡲࡲ࡫࡮ࡵ࠽ࠣࡷࡪࡺࡵࡱࠢࡰࡥࡾࠦࡢࡦࠢ࡬ࡲࡨࡵ࡭ࡱ࡮ࡨࡸࡪ࠴ࠢዩ"))
    return bstack1l1l1l1111l_opy_, bstack1l1l11lll11_opy_
bstack1l1l1111l11_opy_ = bstack1l1lll1_opy_ (u"ࠧ࠿࠹࠺࠻ࠥዪ")
bstack1l11lll111l_opy_ = bstack1l1lll1_opy_ (u"ࠨࡲࡦࡣࡧࡽࠧያ")
bstack1l1ll11l1l1_opy_ = bstack1l1lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡔࡇࡖࡗࡎࡕࡎࡠࡋࡇࠦዬ")
bstack1l1ll111ll1_opy_ = bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡎࡌࡗ࡙ࡋࡎࡠࡃࡇࡈࡗࠨይ")
bstack11lll11111_opy_ = bstack1l1lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠧዮ")
bstack1l11lll11l1_opy_ = re.compile(bstack1l1lll1_opy_ (u"ࡵࠦ࠭ࡅࡩࠪ࠰࠭ࠬࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡿࡆࡘ࠯࠮ࠫࠤዯ"))
bstack1l1ll111l11_opy_ = bstack1l1lll1_opy_ (u"ࠦࡩ࡫ࡶࡦ࡮ࡲࡴࡲ࡫࡮ࡵࠤደ")
bstack1l11llllll1_opy_ = bstack1l1lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡕࡒࡄࡇࡢࡊࡆࡒࡌࡃࡃࡆࡏࠧዱ")
bstack1l11ll1llll_opy_ = [
    Events.bstack11llllll1_opy_,
    Events.CONNECT,
    Events.bstack1l111l1l11_opy_,
]
class SDKCLI:
    _1ll1ll1l1l1_opy_ = None
    process: Union[None, Any]
    bstack1l1ll111lll_opy_: bool
    bstack1l1l1l1l1l1_opy_: bool
    bstack1l1l1l11111_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1l111lll1_opy_: Union[None, grpc.Channel]
    bstack1l1ll11l11l_opy_: str
    test_framework: TestFramework
    bstack111111l11l_opy_: bstack1lll111ll11_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l111ll1l_opy_: bstack1l1l1l1ll1l_opy_
    accessibility: bstack1l1ll11ll11_opy_
    bstack111l1lll11_opy_: bstack11l1llll11_opy_
    ai: bstack1l1ll1l11l1_opy_
    bstack1l1l11lll1l_opy_: bstack1l1l11111ll_opy_
    bstack1l1l111l1ll_opy_: List[bstack1111111ll1_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1ll11l1ll_opy_: Any
    bstack1l1l1111l1l_opy_: Dict[str, timedelta]
    bstack1l11ll1ll1l_opy_: str
    bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_
    def __new__(cls):
        if not cls._1ll1ll1l1l1_opy_:
            cls._1ll1ll1l1l1_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll1l1l1_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1ll111lll_opy_ = False
        self.bstack1l1l111lll1_opy_ = None
        self.bstack1lllll1ll11_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1ll111ll1_opy_, None)
        self.bstack1l1l11ll1l1_opy_ = os.environ.get(bstack1l1ll11l1l1_opy_, bstack1l1lll1_opy_ (u"ࠨࠢዲ")) == bstack1l1lll1_opy_ (u"ࠢࠣዳ")
        self.bstack1l1l1l1l1l1_opy_ = False
        self.bstack1l1l1l11111_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1ll11l1ll_opy_ = None
        self.test_framework = None
        self.bstack111111l11l_opy_ = None
        self.bstack1l1ll11l11l_opy_=bstack1l1lll1_opy_ (u"ࠣࠤዴ")
        self.session_framework = None
        self.logger = bstack111l11l1l_opy_.get_logger(self.__class__.__name__, bstack111l11l1l_opy_.bstack1l11lllll1l_opy_())
        self.bstack1l1l1111l1l_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11lll1l_opy_ = bstack1lll11llll1_opy_()
        self.bstack1l1l11l1111_opy_ = None
        self.bstack1ll1lll111l_opy_ = None
        self.bstack1l1l111ll1l_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l111l1ll_opy_ = []
    def bstack1l1l1l1l1_opy_(self):
        return os.environ.get(bstack11lll11111_opy_).lower().__eq__(bstack1l1lll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢድ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l11llllll1_opy_, bstack1l1lll1_opy_ (u"ࠪࠫዶ")).lower() in [bstack1l1lll1_opy_ (u"ࠫࡹࡸࡵࡦࠩዷ"), bstack1l1lll1_opy_ (u"ࠬ࠷ࠧዸ"), bstack1l1lll1_opy_ (u"࠭ࡹࡦࡵࠪዹ")]:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡇࡱࡵࡧ࡮ࡴࡧࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡱࡴࡪࡥࠡࡦࡸࡩࠥࡺ࡯ࠡࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡑࡕࡇࡊࡥࡆࡂࡎࡏࡆࡆࡉࡋࠡࡧࡱࡺ࡮ࡸ࡯࡯࡯ࡨࡲࡹࠦࡶࡢࡴ࡬ࡥࡧࡲࡥࠣዺ"))
            os.environ[bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦዻ")] = bstack1l1lll1_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣዼ")
            return False
        if bstack1l1lll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧዽ") in config and str(config[bstack1l1lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨዾ")]).lower() != bstack1l1lll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫዿ"):
            return False
        bstack1l11lll1ll1_opy_ = [bstack1l1lll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨጀ"), bstack1l1lll1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦጁ")]
        bstack1l11llll1ll_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦጂ")) in bstack1l11lll1ll1_opy_ or os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪጃ")) in bstack1l11lll1ll1_opy_
        os.environ[bstack1l1lll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨጄ")] = str(bstack1l11llll1ll_opy_) # bstack1l11lll1l1l_opy_ bstack1l1l11llll1_opy_ VAR to bstack1l1ll11111l_opy_ is binary running
        return bstack1l11llll1ll_opy_
    def bstack11llll1ll_opy_(self):
        for event in bstack1l11ll1llll_opy_:
            bstack1llll111ll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1llll111ll_opy_.logger.debug(bstack1l1lll1_opy_ (u"ࠦࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠣࡁࡃࠦࡻࡢࡴࡪࡷࢂࠦࠢጅ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠧࠨጆ"))
            )
        bstack1llll111ll_opy_.register(Events.bstack11llllll1_opy_, self.__1l11lll1l11_opy_)
        bstack1llll111ll_opy_.register(Events.CONNECT, self.__1l1l1l111l1_opy_)
        bstack1llll111ll_opy_.register(Events.bstack1l111l1l11_opy_, self.__1l1l11l1l11_opy_)
        bstack1llll111ll_opy_.register(Events.bstack1l1l1ll1l1_opy_, self.__1l1l11111l1_opy_)
    def bstack11lll11lll_opy_(self):
        return not self.bstack1l1l11ll1l1_opy_ and os.environ.get(bstack1l1ll11l1l1_opy_, bstack1l1lll1_opy_ (u"ࠨࠢጇ")) != bstack1l1lll1_opy_ (u"ࠢࠣገ")
    def is_running(self):
        if self.bstack1l1l11ll1l1_opy_:
            return self.bstack1l1ll111lll_opy_
        else:
            return bool(self.bstack1l1l111lll1_opy_)
    def bstack1l1l111111l_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l111l1ll_opy_) and cli.is_running()
    def __1l1l11l1ll1_opy_(self, bstack1l1l111ll11_opy_=10):
        if self.bstack1lllll1ll11_opy_:
            return
        bstack11ll11ll1_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1ll111ll1_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠣ࡝ࠥጉ") + str(id(self)) + bstack1l1lll1_opy_ (u"ࠤࡠࠤࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡴࡧࠣጊ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1l1lll1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠯ࡧࡱࡥࡧࡲࡥࡠࡪࡷࡸࡵࡥࡰࡳࡱࡻࡽࠧጋ"), 0), (bstack1l1lll1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠰ࡨࡲࡦࡨ࡬ࡦࡡ࡫ࡸࡹࡶࡳࡠࡲࡵࡳࡽࡿࠢጌ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l111ll11_opy_)
        self.bstack1l1l111lll1_opy_ = channel
        self.bstack1lllll1ll11_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1l111lll1_opy_)
        self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡧࡴࡴ࡮ࡦࡥࡷࠦግ"), datetime.now() - bstack11ll11ll1_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1ll111ll1_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤ࠻ࠢ࡬ࡷࡤࡩࡨࡪ࡮ࡧࡣࡵࡸ࡯ࡤࡧࡶࡷࡂࠨጎ") + str(self.bstack11lll11lll_opy_()) + bstack1l1lll1_opy_ (u"ࠢࠣጏ"))
    def __1l1l11l1l11_opy_(self, event_name):
        if self.bstack11lll11lll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡶࡸࡴࡶࡰࡪࡰࡪࠤࡈࡒࡉࠣጐ"))
        self.__1l1l1llll1l_opy_()
    def __1l1l11111l1_opy_(self, event_name, bstack1l1l1ll1l11_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠤ጑"))
        bstack1l1l1111lll_opy_ = Path(bstack1lll1ll1l11_opy_ (u"ࠥࡿࡸ࡫࡬ࡧ࠰ࡦࡰ࡮ࡥࡤࡪࡴࢀ࠳ࡺࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࡸ࠴ࡪࡴࡱࡱࠦጒ"))
        if self.bstack1l1l11lll11_opy_ and bstack1l1l1111lll_opy_.exists():
            with open(bstack1l1l1111lll_opy_, bstack1l1lll1_opy_ (u"ࠫࡷ࠭ጓ"), encoding=bstack1l1lll1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫጔ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"࠭ࡐࡐࡕࡗࠫጕ"), bstack1l111l11l_opy_(bstack11ll1lll1l_opy_), data, {
                        bstack1l1lll1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ጖"): (self.config[bstack1l1lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ጗")], self.config[bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬጘ")])
                    })
                except Exception as e:
                    logger.debug(bstack111l1111l_opy_.format(str(e)))
            bstack1l1l1111lll_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l11ll1ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1l11lll1l11_opy_(self, event_name: str, data):
        from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
        self.bstack1l1ll11l11l_opy_, self.bstack1l1l11lll11_opy_ = bstack1l1l1l11l1l_opy_(data.bs_config)
        os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡ࡚ࡖࡎ࡚ࡁࡃࡎࡈࡣࡉࡏࡒࠨጙ")] = self.bstack1l1l11lll11_opy_
        if not self.bstack1l1ll11l11l_opy_ or not self.bstack1l1l11lll11_opy_:
            raise ValueError(bstack1l1lll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡺࡨࡦࠢࡖࡈࡐࠦࡃࡍࡋࠣࡦ࡮ࡴࡡࡳࡻࠥጚ"))
        if self.bstack11lll11lll_opy_():
            self.__1l1l1l111l1_opy_(event_name, bstack1lll1l1l1l_opy_())
            return
        try:
            bstack1llll1ll11l_opy_.end(EVENTS.bstack1l1lll1lll_opy_.value, EVENTS.bstack1l1lll1lll_opy_.value + bstack1l1lll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧጛ"), EVENTS.bstack1l1lll1lll_opy_.value + bstack1l1lll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦጜ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1l1lll1_opy_ (u"ࠢࡄࡱࡰࡴࡱ࡫ࡴࡦࠢࡖࡈࡐࠦࡓࡦࡶࡸࡴ࠳ࠨጝ"))
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡾࢁࠧጞ").format(e))
        start = datetime.now()
        is_started = self.__1l1l1l11lll_opy_()
        self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠤࡶࡴࡦࡽ࡮ࡠࡶ࡬ࡱࡪࠨጟ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l11l1ll1_opy_()
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤጠ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1l1ll1lll_opy_(data)
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤጡ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l1ll1ll1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1l1l1l111l1_opy_(self, event_name: str, data: bstack1lll1l1l1l_opy_):
        if not self.bstack11lll11lll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥࡲࡲࡳ࡫ࡣࡵ࠼ࠣࡲࡴࡺࠠࡢࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴࠤጢ"))
            return
        bin_session_id = os.environ.get(bstack1l1ll11l1l1_opy_)
        start = datetime.now()
        self.__1l1l11l1ll1_opy_()
        self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧጣ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦࠣࡸࡴࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡅࡏࡍࠥࠨጤ") + str(bin_session_id) + bstack1l1lll1_opy_ (u"ࠣࠤጥ"))
        start = datetime.now()
        self.__1l1l1lllll1_opy_()
        self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢጦ"), datetime.now() - start)
    def __1l11ll1l1ll_opy_(self):
        if not self.bstack1lllll1ll11_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡧࡦࡴ࡮ࡰࡶࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࠦ࡭ࡰࡦࡸࡰࡪࡹࠢጧ"))
            return
        bstack1l1l1llllll_opy_ = {
            bstack1l1lll1_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣጨ"): (bstack1ll1lll1ll1_opy_, bstack1lll1l1l11l_opy_, bstack1lll1l11ll1_opy_),
            bstack1l1lll1_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢጩ"): (bstack1lllll1ll1l_opy_, bstack1lll111l11l_opy_, bstack1lllll111l1_opy_),
        }
        if not self.bstack1l1l11l1111_opy_ and self.session_framework in bstack1l1l1llllll_opy_:
            bstack1l1l111l11l_opy_, bstack1l11llll11l_opy_, bstack1l1l1l111ll_opy_ = bstack1l1l1llllll_opy_[self.session_framework]
            bstack1l1l1ll11l1_opy_ = bstack1l11llll11l_opy_()
            self.bstack1ll1lll111l_opy_ = bstack1l1l1ll11l1_opy_
            self.bstack1l1l11l1111_opy_ = bstack1l1l1l111ll_opy_
            self.bstack1l1l111l1ll_opy_.append(bstack1l1l1ll11l1_opy_)
            self.bstack1l1l111l1ll_opy_.append(bstack1l1l111l11l_opy_(self.bstack1ll1lll111l_opy_))
        if not self.bstack1l1l111ll1l_opy_ and self.config_observability and self.config_observability.success: # bstack1lllll1l1l1_opy_
            self.bstack1l1l111ll1l_opy_ = bstack1l1l1l1ll1l_opy_(self.bstack1l1l11l1111_opy_, self.bstack1ll1lll111l_opy_) # bstack1l1l1l1l111_opy_
            self.bstack1l1l111l1ll_opy_.append(self.bstack1l1l111ll1l_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1ll11ll11_opy_(self.bstack1l1l11l1111_opy_, self.bstack1ll1lll111l_opy_)
            self.bstack1l1l111l1ll_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1l1lll1_opy_ (u"ࠨࡳࡦ࡮ࡩࡌࡪࡧ࡬ࠣጪ"), False) == True:
            self.ai = bstack1l1ll1l11l1_opy_()
            self.bstack1l1l111l1ll_opy_.append(self.ai)
        if not self.percy and self.bstack1l1ll11l1ll_opy_ and self.bstack1l1ll11l1ll_opy_.success:
            self.percy = bstack1l1l11111ll_opy_(self.bstack1l1ll11l1ll_opy_)
            self.bstack1l1l111l1ll_opy_.append(self.percy)
        for mod in self.bstack1l1l111l1ll_opy_:
            if not mod.bstack1lll11lll11_opy_():
                mod.configure(self.bstack1lllll1ll11_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11lll1l_opy_)
    def __1l11llll111_opy_(self):
        for mod in self.bstack1l1l111l1ll_opy_:
            if mod.bstack1lll11lll11_opy_():
                mod.configure(self.bstack1lllll1ll11_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l1l1111111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1l1l1ll1lll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l1l1l1l1_opy_:
            return
        self.__1l1ll111111_opy_(data)
        bstack11ll11ll1_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1l1lll1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢጫ")
        req.sdk_language = bstack1l1lll1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣጬ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l11lll11l1_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤ࡞ࠦጭ") + str(id(self)) + bstack1l1lll1_opy_ (u"ࠥࡡࠥࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡹࡴࡢࡴࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤጮ"))
            r = self.bstack1lllll1ll11_opy_.StartBinSession(req)
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡸࡦࡸࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨጯ"), datetime.now() - bstack11ll11ll1_opy_)
            os.environ[bstack1l1ll11l1l1_opy_] = r.bin_session_id
            self.__1l1l1lll1ll_opy_(r)
            self.__1l11ll1l1ll_opy_()
            self.bstack1lll11lll1l_opy_.start()
            self.bstack1l1l1l1l1l1_opy_ = True
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡡࠢጰ") + str(id(self)) + bstack1l1lll1_opy_ (u"ࠨ࡝ࠡ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠦጱ"))
        except grpc.bstack1l11llll1l1_opy_ as bstack1l1l1l1l1ll_opy_:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡴࡪ࡯ࡨࡳࡪࡻࡴ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤጲ") + str(bstack1l1l1l1l1ll_opy_) + bstack1l1lll1_opy_ (u"ࠣࠤጳ"))
            traceback.print_exc()
            raise bstack1l1l1l1l1ll_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨጴ") + str(e) + bstack1l1lll1_opy_ (u"ࠥࠦጵ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l1lll111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1l1l1lllll1_opy_(self):
        if not self.bstack11lll11lll_opy_() or not self.cli_bin_session_id or self.bstack1l1l1l11111_opy_:
            return
        bstack11ll11ll1_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫጶ"), bstack1l1lll1_opy_ (u"ࠬ࠶ࠧጷ")))
        try:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡛ࠣጸ") + str(id(self)) + bstack1l1lll1_opy_ (u"ࠢ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤጹ"))
            r = self.bstack1lllll1ll11_opy_.ConnectBinSession(req)
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡣࡰࡰࡱࡩࡨࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧጺ"), datetime.now() - bstack11ll11ll1_opy_)
            self.__1l1l1lll1ll_opy_(r)
            self.__1l11ll1l1ll_opy_()
            self.bstack1lll11lll1l_opy_.start()
            self.bstack1l1l1l11111_opy_ = True
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤ࡞ࠦጻ") + str(id(self)) + bstack1l1lll1_opy_ (u"ࠥࡡࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠤጼ"))
        except grpc.bstack1l11llll1l1_opy_ as bstack1l1l1l1l1ll_opy_:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡸ࡮ࡳࡥࡰࡧࡸࡸ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨጽ") + str(bstack1l1l1l1l1ll_opy_) + bstack1l1lll1_opy_ (u"ࠧࠨጾ"))
            traceback.print_exc()
            raise bstack1l1l1l1l1ll_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥጿ") + str(e) + bstack1l1lll1_opy_ (u"ࠢࠣፀ"))
            traceback.print_exc()
            raise e
    def __1l1l1lll1ll_opy_(self, r):
        self.bstack1l1l1l1lll1_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1l1lll1_opy_ (u"ࠣࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡹࡥࡳࡸࡨࡶࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢፁ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1l1lll1_opy_ (u"ࠤࡨࡱࡵࡺࡹࠡࡥࡲࡲ࡫࡯ࡧࠡࡨࡲࡹࡳࡪࠢፂ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1l1lll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡧࡵࡧࡾࠦࡩࡴࠢࡶࡩࡳࡺࠠࡰࡰ࡯ࡽࠥࡧࡳࠡࡲࡤࡶࡹࠦ࡯ࡧࠢࡷ࡬ࡪࠦࠢࡄࡱࡱࡲࡪࡩࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱ࠰ࠧࠦࡡ࡯ࡦࠣࡸ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣ࡭ࡸࠦࡡ࡭ࡵࡲࠤࡺࡹࡥࡥࠢࡥࡽ࡙ࠥࡴࡢࡴࡷࡆ࡮ࡴࡓࡦࡵࡶ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬ࡪࡸࡥࡧࡱࡵࡩ࠱ࠦࡎࡰࡰࡨࠤ࡭ࡧ࡮ࡥ࡮࡬ࡲ࡬ࠦࡩࡴࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧፃ")
        self.bstack1l1ll11l1ll_opy_ = getattr(r, bstack1l1lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪፄ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩፅ")] = self.config_testhub.jwt
        os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫፆ")] = self.config_testhub.build_hashed_id
    def bstack1l1l11lllll_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1ll111lll_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1l1l11ll1_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1l1l11ll1_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1l11lllll_opy_(event_name=EVENTS.bstack1l1l11l1lll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1l1l1l11lll_opy_(self, bstack1l1l111ll11_opy_=10):
        if self.bstack1l1ll111lll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡴࡶࡤࡶࡹࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡴࡸࡲࡳ࡯࡮ࡨࠤፇ"))
            return True
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡵࡷࡥࡷࡺࠢፈ"))
        if os.getenv(bstack1l1lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡋࡎࡗࠤፉ")) == bstack1l1ll111l11_opy_:
            self.cli_bin_session_id = bstack1l1ll111l11_opy_
            self.cli_listen_addr = bstack1l1lll1_opy_ (u"ࠥࡹࡳ࡯ࡸ࠻࠱ࡷࡱࡵ࠵ࡳࡥ࡭࠰ࡴࡱࡧࡴࡧࡱࡵࡱ࠲ࠫࡳ࠯ࡵࡲࡧࡰࠨፊ") % (self.cli_bin_session_id)
            self.bstack1l1ll111lll_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1ll11l11l_opy_, bstack1l1lll1_opy_ (u"ࠦࡸࡪ࡫ࠣፋ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l11ll11l_opy_ compat for text=True in bstack1l11ll1lll1_opy_ python
            encoding=bstack1l1lll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦፌ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1ll1111ll_opy_ = threading.Thread(target=self.__1l1l1ll1111_opy_, args=(bstack1l1l111ll11_opy_,))
        bstack1l1ll1111ll_opy_.start()
        bstack1l1ll1111ll_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡹࡰࡢࡹࡱ࠾ࠥࡸࡥࡵࡷࡵࡲࡨࡵࡤࡦ࠿ࡾࡷࡪࡲࡦ࠯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡵࡩࡹࡻࡲ࡯ࡥࡲࡨࡪࢃࠠࡰࡷࡷࡁࢀࡹࡥ࡭ࡨ࠱ࡴࡷࡵࡣࡦࡵࡶ࠲ࡸࡺࡤࡰࡷࡷ࠲ࡷ࡫ࡡࡥࠪࠬࢁࠥ࡫ࡲࡳ࠿ࠥፍ") + str(self.process.stderr.read()) + bstack1l1lll1_opy_ (u"ࠢࠣፎ"))
        if not self.bstack1l1ll111lll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣ࡝ࠥፏ") + str(id(self)) + bstack1l1lll1_opy_ (u"ࠤࡠࠤࡨࡲࡥࡢࡰࡸࡴࠧፐ"))
            self.__1l1l1llll1l_opy_()
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡳࡶࡴࡩࡥࡴࡵࡢࡶࡪࡧࡤࡺ࠼ࠣࠦፑ") + str(self.bstack1l1ll111lll_opy_) + bstack1l1lll1_opy_ (u"ࠦࠧፒ"))
        return self.bstack1l1ll111lll_opy_
    def __1l1l1ll1111_opy_(self, bstack1l1l1ll11ll_opy_=10):
        bstack1l1l111llll_opy_ = time.time()
        while self.process and time.time() - bstack1l1l111llll_opy_ < bstack1l1l1ll11ll_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1l1lll1_opy_ (u"ࠧ࡯ࡤ࠾ࠤፓ") in line:
                    self.cli_bin_session_id = line.split(bstack1l1lll1_opy_ (u"ࠨࡩࡥ࠿ࠥፔ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡤ࡮࡬ࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨ࠿ࠨፕ") + str(self.cli_bin_session_id) + bstack1l1lll1_opy_ (u"ࠣࠤፖ"))
                    continue
                if bstack1l1lll1_opy_ (u"ࠤ࡯࡭ࡸࡺࡥ࡯࠿ࠥፗ") in line:
                    self.cli_listen_addr = line.split(bstack1l1lll1_opy_ (u"ࠥࡰ࡮ࡹࡴࡦࡰࡀࠦፘ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡨࡲࡩࡠ࡮࡬ࡷࡹ࡫࡮ࡠࡣࡧࡨࡷࡀࠢፙ") + str(self.cli_listen_addr) + bstack1l1lll1_opy_ (u"ࠧࠨፚ"))
                    continue
                if bstack1l1lll1_opy_ (u"ࠨࡰࡰࡴࡷࡁࠧ፛") in line:
                    port = line.split(bstack1l1lll1_opy_ (u"ࠢࡱࡱࡵࡸࡂࠨ፜"))[-1:][0].strip()
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡲࡲࡶࡹࡀࠢ፝") + str(port) + bstack1l1lll1_opy_ (u"ࠤࠥ፞"))
                    continue
                if line.strip() == bstack1l11lll111l_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1l1lll1_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡌࡓࡤ࡙ࡔࡓࡇࡄࡑࠧ፟"), bstack1l1lll1_opy_ (u"ࠦ࠶ࠨ፠")) == bstack1l1lll1_opy_ (u"ࠧ࠷ࠢ፡"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1ll111lll_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡥࡳࡴࡲࡶ࠿ࠦࠢ።") + str(e) + bstack1l1lll1_opy_ (u"ࠢࠣ፣"))
        return False
    @measure(event_name=EVENTS.bstack1l1l11l11l1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1l1l1llll1l_opy_(self):
        if self.bstack1l1l111lll1_opy_:
            self.bstack1lll11lll1l_opy_.stop()
            start = datetime.now()
            if self.bstack1l1ll111l1l_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l1l11111_opy_:
                    self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠣࡵࡷࡳࡵࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧ፤"), datetime.now() - start)
                else:
                    self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠤࡶࡸࡴࡶ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨ፥"), datetime.now() - start)
            self.__1l11llll111_opy_()
            start = datetime.now()
            self.bstack1l1l111lll1_opy_.close()
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠥࡨ࡮ࡹࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧ፦"), datetime.now() - start)
            self.bstack1l1l111lll1_opy_ = None
        if self.process:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡸࡺ࡯ࡱࠤ፧"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠧࡱࡩ࡭࡮ࡢࡸ࡮ࡳࡥࠣ፨"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l11ll1l1_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1lll111l1_opy_()
                self.logger.info(
                    bstack1l1lll1_opy_ (u"ࠨࡖࡪࡵ࡬ࡸࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠢࡷࡳࠥࡼࡩࡦࡹࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡵࡵࡲࡵ࠮ࠣ࡭ࡳࡹࡩࡨࡪࡷࡷ࠱ࠦࡡ࡯ࡦࠣࡱࡦࡴࡹࠡ࡯ࡲࡶࡪࠦࡤࡦࡤࡸ࡫࡬࡯࡮ࡨࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮࡯ࠤࡦࡺࠠࡰࡰࡨࠤࡵࡲࡡࡤࡧࠤࡠࡳࠨ፩").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1l1lll1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭፪")] = self.config_testhub.build_hashed_id
        self.bstack1l1ll111lll_opy_ = False
    def __1l1ll111111_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1l1lll1_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ፫")] = selenium.__version__
            data.frameworks.append(bstack1l1lll1_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦ፬"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1l1lll1_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ፭")] = __version__
            data.frameworks.append(bstack1l1lll1_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ፮"))
        except:
            pass
    def bstack1l1l11l1l1l_opy_(self, hub_url: str, platform_index: int, bstack11ll11l111_opy_: Any):
        if self.bstack111111l11l_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠦࡳࡦࡶࡸࡴࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡶࡩࡹࠦࡵࡱࠤ፯"))
            return
        try:
            bstack11ll11ll1_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1l1lll1_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ፰")
            self.bstack111111l11l_opy_ = bstack1lllll111l1_opy_(
                cli.config.get(bstack1l1lll1_opy_ (u"ࠢࡩࡷࡥ࡙ࡷࡲࠢ፱"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1lllllll11l_opy_={bstack1l1lll1_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡩࡶࡴࡳ࡟ࡤࡣࡳࡷࠧ፲"): bstack11ll11l111_opy_}
            )
            def bstack1l11lll1lll_opy_(self):
                return
            if self.config.get(bstack1l1lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠦ፳"), True):
                Service.start = bstack1l11lll1lll_opy_
                Service.stop = bstack1l11lll1lll_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack11l1llll11_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll1111ll1l_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠦ፴"), datetime.now() - bstack11ll11ll1_opy_)
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠻ࠢࠥ፵") + str(e) + bstack1l1lll1_opy_ (u"ࠧࠨ፶"))
    def bstack1l1l11l11ll_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack11l1ll1lll_opy_
            self.bstack111111l11l_opy_ = bstack1lll1l11ll1_opy_(
                platform_index,
                framework_name=bstack1l1lll1_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ፷"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡀࠠࠣ፸") + str(e) + bstack1l1lll1_opy_ (u"ࠣࠤ፹"))
            pass
    def bstack1l1l1ll111l_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠣࡷࡪࡺࡵࡱࠢࡳࡽࡹ࡫ࡳࡵ࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡸ࡫ࡴࠡࡷࡳࠦ፺"))
            return
        if bstack1l1l1lll1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1l1lll1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ፻"): pytest.__version__ }, [bstack1l1lll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣ፼")], self.bstack1lll11lll1l_opy_, self.bstack1lllll1ll11_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l11lll1111_opy_({ bstack1l1lll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ፽"): pytest.__version__ }, [bstack1l1lll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨ፾")], self.bstack1lll11lll1l_opy_, self.bstack1lllll1ll11_opy_)
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡽࡹ࡫ࡳࡵ࠼ࠣࠦ፿") + str(e) + bstack1l1lll1_opy_ (u"ࠣࠤᎀ"))
        self.bstack1l1l1lll1l1_opy_()
    def bstack1l1l1lll1l1_opy_(self):
        if not self.bstack1l1l1l1l1_opy_():
            return
        bstack111l1llll1_opy_ = None
        def bstack1lll1ll111_opy_(config, startdir):
            return bstack1l1lll1_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿ࠵ࢃࠢᎁ").format(bstack1l1lll1_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤᎂ"))
        def bstack11l1l1ll11_opy_():
            return
        def bstack11l1l1ll1l_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1l1lll1_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫᎃ"):
                return bstack1l1lll1_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦᎄ")
            else:
                return bstack111l1llll1_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack111l1llll1_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1lll1ll111_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11l1l1ll11_opy_
            Config.getoption = bstack11l1l1ll1l_opy_
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡹࡩࡨࠡࡲࡼࡸࡪࡹࡴࠡࡵࡨࡰࡪࡴࡩࡶ࡯ࠣࡪࡴࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡀࠠࠣᎅ") + str(e) + bstack1l1lll1_opy_ (u"ࠢࠣᎆ"))
    def bstack1l11lll11ll_opy_(self):
        bstack11ll11111l_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack11ll11111l_opy_, dict):
            if cli.config_observability:
                bstack11ll11111l_opy_.update(
                    {bstack1l1lll1_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣᎇ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1l1lll1_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࡣࡹࡵ࡟ࡸࡴࡤࡴࠧᎈ") in accessibility.get(bstack1l1lll1_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦᎉ"), {}):
                    bstack1l1l111l111_opy_ = accessibility.get(bstack1l1lll1_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᎊ"))
                    bstack1l1l111l111_opy_.update({ bstack1l1lll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࡔࡰ࡙ࡵࡥࡵࠨᎋ"): bstack1l1l111l111_opy_.pop(bstack1l1lll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡠࡶࡲࡣࡼࡸࡡࡱࠤᎌ")) })
                bstack11ll11111l_opy_.update({bstack1l1lll1_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢᎍ"): accessibility })
        return bstack11ll11111l_opy_
    @measure(event_name=EVENTS.bstack1l1l1l11l11_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l1ll111l1l_opy_(self, bstack1l1l1llll11_opy_: str = None, bstack1l11lllllll_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1lllll1ll11_opy_:
            return
        bstack11ll11ll1_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1llll11_opy_:
            req.bstack1l1l1llll11_opy_ = bstack1l1l1llll11_opy_
        if bstack1l11lllllll_opy_:
            req.bstack1l11lllllll_opy_ = bstack1l11lllllll_opy_
        try:
            r = self.bstack1lllll1ll11_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡵࡱࡳࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᎎ"), datetime.now() - bstack11ll11ll1_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1111l11111_opy_(self, key: str, value: timedelta):
        tag = bstack1l1lll1_opy_ (u"ࠤࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴࠤᎏ") if self.bstack11lll11lll_opy_() else bstack1l1lll1_opy_ (u"ࠥࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴࠤ᎐")
        self.bstack1l1l1111l1l_opy_[bstack1l1lll1_opy_ (u"ࠦ࠿ࠨ᎑").join([tag + bstack1l1lll1_opy_ (u"ࠧ࠳ࠢ᎒") + str(id(self)), key])] += value
    def bstack1lll111l1_opy_(self):
        if not os.getenv(bstack1l1lll1_opy_ (u"ࠨࡄࡆࡄࡘࡋࡤࡖࡅࡓࡈࠥ᎓"), bstack1l1lll1_opy_ (u"ࠢ࠱ࠤ᎔")) == bstack1l1lll1_opy_ (u"ࠣ࠳ࠥ᎕"):
            return
        bstack1l1l1ll1l1l_opy_ = dict()
        bstack1lll1l1l1l1_opy_ = []
        if self.test_framework:
            bstack1lll1l1l1l1_opy_.extend(list(self.test_framework.bstack1lll1l1l1l1_opy_.values()))
        if self.bstack111111l11l_opy_:
            bstack1lll1l1l1l1_opy_.extend(list(self.bstack111111l11l_opy_.bstack1lll1l1l1l1_opy_.values()))
        for instance in bstack1lll1l1l1l1_opy_:
            if not instance.platform_index in bstack1l1l1ll1l1l_opy_:
                bstack1l1l1ll1l1l_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l1ll1l1l_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll1ll11_opy_().items():
                report[k] += v
                report[k.split(bstack1l1lll1_opy_ (u"ࠤ࠽ࠦ᎖"))[0]] += v
        bstack1l1l1lll11l_opy_ = sorted([(k, v) for k, v in self.bstack1l1l1111l1l_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l1l1l11l_opy_ = 0
        for r in bstack1l1l1lll11l_opy_:
            bstack1l11lllll11_opy_ = r[1].total_seconds()
            bstack1l1l1l1l11l_opy_ += bstack1l11lllll11_opy_
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡧࡱ࡯࠺ࡼࡴ࡞࠴ࡢࢃ࠽ࠣ᎗") + str(bstack1l11lllll11_opy_) + bstack1l1lll1_opy_ (u"ࠦࠧ᎘"))
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠧ࠳࠭ࠣ᎙"))
        bstack1l1l11ll111_opy_ = []
        for platform_index, report in bstack1l1l1ll1l1l_opy_.items():
            bstack1l1l11ll111_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l11ll111_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll11lll_opy_ = set()
        bstack1l1l1111ll1_opy_ = 0
        for r in bstack1l1l11ll111_opy_:
            bstack1l11lllll11_opy_ = r[2].total_seconds()
            bstack1l1l1111ll1_opy_ += bstack1l11lllll11_opy_
            bstack1lll11lll_opy_.add(r[0])
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡴࡦࡵࡷ࠾ࡵࡲࡡࡵࡨࡲࡶࡲ࠳ࡻࡳ࡝࠳ࡡࢂࡀࡻࡳ࡝࠴ࡡࢂࡃࠢ᎚") + str(bstack1l11lllll11_opy_) + bstack1l1lll1_opy_ (u"ࠢࠣ᎛"))
        if self.bstack11lll11lll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣ࠯࠰ࠦ᎜"))
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡃࡻࡵࡱࡷࡥࡱࡥࡣ࡭࡫ࢀࠤࡹ࡫ࡳࡵ࠼ࡳࡰࡦࡺࡦࡰࡴࡰࡷ࠲ࢁࡳࡵࡴࠫࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠯ࡽ࠾ࠤ᎝") + str(bstack1l1l1111ll1_opy_) + bstack1l1lll1_opy_ (u"ࠥࠦ᎞"))
        else:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹ࠽ࠣ᎟") + str(bstack1l1l1l1l11l_opy_) + bstack1l1lll1_opy_ (u"ࠧࠨᎠ"))
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࠭࠮ࠤᎡ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1lllll1ll11_opy_:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡤ࡮࡬ࡣࡸ࡫ࡲࡷ࡫ࡦࡩࠥ࡯ࡳࠡࡰࡲࡸࠥ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࡦ࠱ࠤࡈࡧ࡮࡯ࡱࡷࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦᎢ"))
            return None
        response = self.bstack1lllll1ll11_opy_.TestOrchestration(request)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡶࡨࡷࡹ࠳࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠳ࡳࡦࡵࡶ࡭ࡴࡴ࠽ࡼࡿࠥᎣ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l1l1lll1_opy_(self, r):
        if r is not None and getattr(r, bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࠪᎤ"), None) and getattr(r.testhub, bstack1l1lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪᎥ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1l1lll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᎦ")))
            for bstack1l1l11l111l_opy_, err in errors.items():
                if err[bstack1l1lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪᎧ")] == bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᎨ"):
                    self.logger.info(err[bstack1l1lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᎩ")])
                else:
                    self.logger.error(err[bstack1l1lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᎪ")])
    def bstack1l1lll1l1_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()