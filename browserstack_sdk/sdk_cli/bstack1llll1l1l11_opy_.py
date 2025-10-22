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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1llll1l1l1l_opy_,
    bstack1lllllll111_opy_,
    bstack1lll111ll11_opy_,
    bstack1llll11l1ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1lllllll11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_, bstack1lll1l1ll11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1llllllllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll11l_opy_ import bstack1llll1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1lll1llllll_opy_
from bstack_utils.helper import bstack1l1111llll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1111ll11ll_opy_ import bstack1llllll1ll1_opy_
import grpc
import traceback
import json
class bstack1l1l1lll111_opy_(bstack1llllllllll_opy_):
    bstack1l1ll11l1ll_opy_ = False
    bstack1l111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤᑎ")
    bstack1l1111l111l_opy_ = bstack11l1l11_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣᑏ")
    bstack1l111l111ll_opy_ = bstack11l1l11_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩ࡯࡫ࡷࠦᑐ")
    bstack1l111l11ll1_opy_ = bstack11l1l11_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡵࡢࡷࡨࡧ࡮࡯࡫ࡱ࡫ࠧᑑ")
    bstack1l11111lll1_opy_ = bstack11l1l11_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲࡠࡪࡤࡷࡤࡻࡲ࡭ࠤᑒ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l11111l1_opy_, bstack1ll1lll1111_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111ll1111_opy_ = False
        self.bstack1l111l1l1l1_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l1l1111_opy_ = bstack1ll1lll1111_opy_
        bstack1l1l11111l1_opy_.bstack1llll1ll1ll_opy_((bstack1llll1l1l1l_opy_.bstack1lllll111ll_opy_, bstack1lllllll111_opy_.PRE), self.bstack1l1111l1l11_opy_)
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1lll11l1ll1_opy_)
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1llll111lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11l1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111ll1ll_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
        if self.bstack1l111ll1111_opy_:
            self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᑓ")] = f.get_state(instance, TestFramework.bstack1llll111ll1_opy_)
        if bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᑔ") in instance.bstack1l1lll1ll11_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llll1lll11_opy_)
            self.accessibility = self.bstack1l111l11111_opy_(tags, self.config[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᑕ")][platform_index])
        else:
            capabilities = self.bstack1l11l1l1111_opy_.bstack1lll1l11l1l_opy_(f, instance, bstack1llllll11l1_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᑖ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠨࠢᑗ"))
                return
            self.accessibility = self.bstack1l111l11111_opy_(tags, capabilities)
        if self.bstack1l11l1l1111_opy_.pages and self.bstack1l11l1l1111_opy_.pages.values():
            bstack1l111l11lll_opy_ = list(self.bstack1l11l1l1111_opy_.pages.values())
            if bstack1l111l11lll_opy_ and isinstance(bstack1l111l11lll_opy_[0], (list, tuple)) and bstack1l111l11lll_opy_[0]:
                bstack1l1111ll1l1_opy_ = bstack1l111l11lll_opy_[0][0]
                if callable(bstack1l1111ll1l1_opy_):
                    page = bstack1l1111ll1l1_opy_()
                    def bstack1111l11111_opy_():
                        self.get_accessibility_results(page, bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᑘ"))
                    def bstack1l1111ll11l_opy_():
                        self.get_accessibility_results_summary(page, bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᑙ"))
                    setattr(page, bstack11l1l11_opy_ (u"ࠤࡪࡩࡹࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡗ࡫ࡳࡶ࡮ࡷࡷࠧᑚ"), bstack1111l11111_opy_)
                    setattr(page, bstack11l1l11_opy_ (u"ࠥ࡫ࡪࡺࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡘࡥࡴࡷ࡯ࡸࡘࡻ࡭࡮ࡣࡵࡽࠧᑛ"), bstack1l1111ll11l_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡸ࡮࡯ࡶ࡮ࡧࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡸࡤࡰࡺ࡫࠽ࠣᑜ") + str(self.accessibility) + bstack11l1l11_opy_ (u"ࠧࠨᑝ"))
    def bstack1l1111l1l11_opy_(
        self,
        f: bstack1lllllll11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        bstack1llllll11l1_opy_: Tuple[bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1ll1111ll_opy_ = datetime.now()
            self.bstack1l1111l1ll1_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡮ࡴࡩࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡦࡳࡳ࡬ࡩࡨࠤᑞ"), datetime.now() - bstack1ll1111ll_opy_)
            if (
                not f.bstack1l1ll1l1l1l_opy_(method_name)
                or f.bstack1l1ll1l11l1_opy_(method_name, *args)
                or f.bstack1l1lll11lll_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l1lll111_opy_.bstack1l111l111ll_opy_, False):
                if not bstack1l1l1lll111_opy_.bstack1l1ll11l1ll_opy_:
                    self.logger.warning(bstack11l1l11_opy_ (u"ࠢ࡜ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࠥᑟ") + str(f.platform_index) + bstack11l1l11_opy_ (u"ࠣ࡟ࠣࡥ࠶࠷ࡹࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡩࡣࡹࡩࠥࡴ࡯ࡵࠢࡥࡩࡪࡴࠠࡴࡧࡷࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᑠ"))
                    bstack1l1l1lll111_opy_.bstack1l1ll11l1ll_opy_ = True
                return
            bstack1l111ll11l1_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111ll11l1_opy_:
                platform_index = f.get_state(instance, bstack1lllllll11l_opy_.bstack1llll1lll11_opy_, 0)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡱࡳࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࡾࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᑡ") + str(f.framework_name) + bstack11l1l11_opy_ (u"ࠥࠦᑢ"))
                return
            command_name = f.bstack1l1ll1llll1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࠨᑣ") + str(method_name) + bstack11l1l11_opy_ (u"ࠧࠨᑤ"))
                return
            bstack1l11111l1ll_opy_ = f.get_state(instance, bstack1l1l1lll111_opy_.bstack1l11111lll1_opy_, False)
            if command_name == bstack11l1l11_opy_ (u"ࠨࡧࡦࡶࠥᑥ") and not bstack1l11111l1ll_opy_:
                f.bstack1llllll1l11_opy_(instance, bstack1l1l1lll111_opy_.bstack1l11111lll1_opy_, True)
                bstack1l11111l1ll_opy_ = True
            if not bstack1l11111l1ll_opy_ and not self.bstack1l111ll1111_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡯ࡱ࡙ࠣࡗࡒࠠ࡭ࡱࡤࡨࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑦ") + str(command_name) + bstack11l1l11_opy_ (u"ࠣࠤᑧ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡱࡳࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑨ") + str(command_name) + bstack11l1l11_opy_ (u"ࠥࠦᑩ"))
                return
            self.logger.info(bstack11l1l11_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠥࢁ࡬ࡦࡰࠫࡷࡨࡸࡩࡱࡶࡶࡣࡹࡵ࡟ࡳࡷࡱ࠭ࢂࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑪ") + str(command_name) + bstack11l1l11_opy_ (u"ࠧࠨᑫ"))
            scripts = [(s, bstack1l111ll11l1_opy_[s]) for s in scripts_to_run if s in bstack1l111ll11l1_opy_]
            for script_name, bstack1lll1lll111_opy_ in scripts:
                try:
                    bstack1ll1111ll_opy_ = datetime.now()
                    if script_name == bstack11l1l11_opy_ (u"ࠨࡳࡤࡣࡱࠦᑬ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿ࠨᑭ") + script_name, datetime.now() - bstack1ll1111ll_opy_)
                    if isinstance(result, dict) and not result.get(bstack11l1l11_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴࠤᑮ"), True):
                        self.logger.warning(bstack11l1l11_opy_ (u"ࠤࡶ࡯࡮ࡶࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡶࡪࡳࡡࡪࡰ࡬ࡲ࡬ࠦࡳࡤࡴ࡬ࡴࡹࡹ࠺ࠡࠤᑯ") + str(result) + bstack11l1l11_opy_ (u"ࠥࠦᑰ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11l1l11_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡳࡤࡴ࡬ࡴࡹࡃࡻࡴࡥࡵ࡭ࡵࡺ࡟࡯ࡣࡰࡩࢂࠦࡥࡳࡴࡲࡶࡂࠨᑱ") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨᑲ"))
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧࠣࡩࡷࡸ࡯ࡳ࠿ࠥᑳ") + str(e) + bstack11l1l11_opy_ (u"ࠢࠣᑴ"))
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111ll1ll_opy_(instance, args)
        capabilities = self.bstack1l11l1l1111_opy_.bstack1lll1l11l1l_opy_(f, instance, bstack1llllll11l1_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111l11111_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧᑵ"))
            return
        driver = self.bstack1l11l1l1111_opy_.bstack1lll1ll1111_opy_(f, instance, bstack1llllll11l1_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1l1llllllll_opy_)
        if not test_name:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᑶ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1llll111ll1_opy_)
        if not test_uuid:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣᑷ"))
            return
        if isinstance(self.bstack1l11l1l1111_opy_, bstack1llll1111ll_opy_):
            framework_name = bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᑸ")
        else:
            framework_name = bstack11l1l11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧᑹ")
        self.bstack1111l111_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1l11llll_opy_ = bstack1llllll1ll1_opy_.bstack1ll1l11l111_opy_(EVENTS.bstack111111ll11_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࠢᑺ"))
            return
        bstack1ll1111ll_opy_ = datetime.now()
        bstack1lll1lll111_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l11_opy_ (u"ࠢࡴࡥࡤࡲࠧᑻ"), None)
        if not bstack1lll1lll111_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪࡷࡨࡧ࡮ࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᑼ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠤࠣࠦᑽ"))
            return
        if self.bstack1l111ll1111_opy_:
            arg = dict()
            arg[bstack11l1l11_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥᑾ")] = method if method else bstack11l1l11_opy_ (u"ࠦࠧᑿ")
            arg[bstack11l1l11_opy_ (u"ࠧࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠧᒀ")] = self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩࠨᒁ")]
            arg[bstack11l1l11_opy_ (u"ࠢࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠧᒂ")] = self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹ࡮ࡵࡣࡡࡥࡹ࡮ࡲࡤࡠࡷࡸ࡭ࡩࠨᒃ")]
            arg[bstack11l1l11_opy_ (u"ࠤࡤࡹࡹ࡮ࡈࡦࡣࡧࡩࡷࠨᒄ")] = self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠣᒅ")]
            arg[bstack11l1l11_opy_ (u"ࠦࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠣᒆ")] = self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠧࡺࡨࡠ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠦᒇ")]
            arg[bstack11l1l11_opy_ (u"ࠨࡳࡤࡣࡱࡘ࡮ࡳࡥࡴࡶࡤࡱࡵࠨᒈ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111l1ll11_opy_ = bstack1lll1lll111_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l1ll11_opy_)
            return
        instance = bstack1lll111ll11_opy_.bstack1l1lll1l1l1_opy_(driver)
        if instance:
            if not bstack1lll111ll11_opy_.get_state(instance, bstack1l1l1lll111_opy_.bstack1l111l11ll1_opy_, False):
                bstack1lll111ll11_opy_.bstack1llllll1l11_opy_(instance, bstack1l1l1lll111_opy_.bstack1l111l11ll1_opy_, True)
            else:
                self.logger.info(bstack11l1l11_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡱࠤࡵࡸ࡯ࡨࡴࡨࡷࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡀࠦᒉ") + str(method) + bstack11l1l11_opy_ (u"ࠣࠤᒊ"))
                return
        self.logger.info(bstack11l1l11_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡃࠢᒋ") + str(method) + bstack11l1l11_opy_ (u"ࠥࠦᒌ"))
        if framework_name == bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒍ"):
            result = self.bstack1l11l1l1111_opy_.bstack1llll1111l1_opy_(driver, bstack1lll1lll111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll111_opy_, {bstack11l1l11_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᒎ"): method if method else bstack11l1l11_opy_ (u"ࠨࠢᒏ")})
        bstack1llllll1ll1_opy_.end(EVENTS.bstack111111ll11_opy_.value, bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᒐ"), bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᒑ"), True, None, command=method)
        if instance:
            bstack1lll111ll11_opy_.bstack1llllll1l11_opy_(instance, bstack1l1l1lll111_opy_.bstack1l111l11ll1_opy_, False)
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࠨᒒ"), datetime.now() - bstack1ll1111ll_opy_)
        return result
        def bstack1l111l1llll_opy_(self, driver: object, framework_name, bstack1ll111l11_opy_: str):
            self.bstack1lllll1l111_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111l1l1l_opy_ = self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᒓ")]
            req.bstack1ll111l11_opy_ = bstack1ll111l11_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llllllll11_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᒔ") + str(r) + bstack11l1l11_opy_ (u"ࠧࠨᒕ"))
                else:
                    bstack1l111l11l1l_opy_ = json.loads(r.bstack1l111l1l11l_opy_.decode(bstack11l1l11_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᒖ")))
                    if bstack1ll111l11_opy_ == bstack11l1l11_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫᒗ"):
                        return bstack1l111l11l1l_opy_.get(bstack11l1l11_opy_ (u"ࠣࡦࡤࡸࡦࠨᒘ"), [])
                    else:
                        return bstack1l111l11l1l_opy_.get(bstack11l1l11_opy_ (u"ࠤࡧࡥࡹࡧࠢᒙ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11l1l11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡶࡰࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࠡࡨࡵࡳࡲࠦࡣ࡭࡫࠽ࠤࠧᒚ") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧᒛ"))
    @measure(event_name=EVENTS.bstack11llll1l11_opy_, stage=STAGE.bstack111llllll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᒜ"))
            return
        if self.bstack1l111ll1111_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡧࡰࡱࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᒝ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack11l1l11_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᒞ"))
        bstack1lll1lll111_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒟ"), None)
        if not bstack1lll1lll111_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᒠ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠥࠦᒡ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1ll1111ll_opy_ = datetime.now()
        if framework_name == bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒢ"):
            result = self.bstack1l11l1l1111_opy_.bstack1llll1111l1_opy_(driver, bstack1lll1lll111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll111_opy_)
        instance = bstack1lll111ll11_opy_.bstack1l1lll1l1l1_opy_(driver)
        if instance:
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࠣᒣ"), datetime.now() - bstack1ll1111ll_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1ll1l1ll_opy_, stage=STAGE.bstack111llllll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࡣࡸࡻ࡭࡮ࡣࡵࡽ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᒤ"))
            return
        if self.bstack1l111ll1111_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack11l1l11_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫᒥ"))
        bstack1lll1lll111_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧᒦ"), None)
        if not bstack1lll1lll111_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᒧ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠥࠦᒨ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1ll1111ll_opy_ = datetime.now()
        if framework_name == bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒩ"):
            result = self.bstack1l11l1l1111_opy_.bstack1llll1111l1_opy_(driver, bstack1lll1lll111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll111_opy_)
        instance = bstack1lll111ll11_opy_.bstack1l1lll1l1l1_opy_(driver)
        if instance:
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࡠࡵࡸࡱࡲࡧࡲࡺࠤᒪ"), datetime.now() - bstack1ll1111ll_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l1lll1_opy_, stage=STAGE.bstack111llllll_opy_)
    def bstack1l11111llll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llllllll11_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᒫ") + str(r) + bstack11l1l11_opy_ (u"ࠢࠣᒬ"))
            else:
                self.bstack1l111l111l1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᒭ") + str(e) + bstack11l1l11_opy_ (u"ࠤࠥᒮ"))
            traceback.print_exc()
            raise e
    def bstack1l111l111l1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡰࡴࡧࡤࡠࡥࡲࡲ࡫࡯ࡧ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥᒯ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111ll1111_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠤᒰ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111l1l1l1_opy_[bstack11l1l11_opy_ (u"ࠧࡺࡨࡠ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠦᒱ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111l1l1l1_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l1111lll11_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111ll11ll_opy_ and command.module == self.bstack1l1111l111l_opy_:
                        if command.method and not command.method in bstack1l1111lll11_opy_:
                            bstack1l1111lll11_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l1111lll11_opy_[command.method]:
                            bstack1l1111lll11_opy_[command.method][command.name] = list()
                        bstack1l1111lll11_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l1111lll11_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l1111l1ll1_opy_(
        self,
        f: bstack1lllllll11l_opy_,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l1l1111_opy_, bstack1llll1111ll_opy_) and method_name != bstack11l1l11_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࠧᒲ"):
            return
        if bstack1lll111ll11_opy_.bstack111111111l_opy_(instance, bstack1l1l1lll111_opy_.bstack1l111l111ll_opy_):
            return
        if f.bstack1lllllllll1_opy_(method_name, *args):
            bstack1l1111l11l1_opy_ = False
            desired_capabilities = f.bstack1l1ll1lll1l_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll11l1l_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllllll11l_opy_.bstack1llll1lll11_opy_, 0)
                bstack1l1111l1111_opy_ = datetime.now()
                r = self.bstack1l11111llll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡩ࡯࡯ࡨ࡬࡫ࠧᒳ"), datetime.now() - bstack1l1111l1111_opy_)
                bstack1l1111l11l1_opy_ = r.success
            else:
                self.logger.error(bstack11l1l11_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡧࡩࡸ࡯ࡲࡦࡦࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠿ࠥᒴ") + str(desired_capabilities) + bstack11l1l11_opy_ (u"ࠤࠥᒵ"))
            f.bstack1llllll1l11_opy_(instance, bstack1l1l1lll111_opy_.bstack1l111l111ll_opy_, bstack1l1111l11l1_opy_)
    def bstack1l111lll11_opy_(self, test_tags):
        bstack1l11111llll_opy_ = self.config.get(bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᒶ"))
        if not bstack1l11111llll_opy_:
            return True
        try:
            include_tags = bstack1l11111llll_opy_[bstack11l1l11_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒷ")] if bstack11l1l11_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒸ") in bstack1l11111llll_opy_ and isinstance(bstack1l11111llll_opy_[bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒹ")], list) else []
            exclude_tags = bstack1l11111llll_opy_[bstack11l1l11_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒺ")] if bstack11l1l11_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒻ") in bstack1l11111llll_opy_ and isinstance(bstack1l11111llll_opy_[bstack11l1l11_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒼ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥᒽ") + str(error))
        return False
    def bstack1ll1l1ll1_opy_(self, caps):
        try:
            if self.bstack1l111ll1111_opy_:
                bstack1l1111lll1l_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥᒾ"))
                if bstack1l1111lll1l_opy_ is not None and str(bstack1l1111lll1l_opy_).lower() == bstack11l1l11_opy_ (u"ࠧࡧ࡮ࡥࡴࡲ࡭ࡩࠨᒿ"):
                    bstack1l11111ll1l_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠨࡡࡱࡲ࡬ࡹࡲࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᓀ")) or caps.get(bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᓁ"))
                    if bstack1l11111ll1l_opy_ is not None and int(bstack1l11111ll1l_opy_) < 11:
                        self.logger.warning(bstack11l1l11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡃࡱࡨࡷࡵࡩࡥࠢ࠴࠵ࠥࡧ࡮ࡥࠢࡤࡦࡴࡼࡥ࠯ࠢࡆࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡼࡥࡳࡵ࡬ࡳࡳࠦ࠽ࠣᓂ") + str(bstack1l11111ll1l_opy_) + bstack11l1l11_opy_ (u"ࠤࠥᓃ"))
                        return False
                return True
            bstack1l1111l1lll_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᓄ"), {}).get(bstack11l1l11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᓅ"), caps.get(bstack11l1l11_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᓆ"), bstack11l1l11_opy_ (u"࠭ࠧᓇ")))
            if bstack1l1111l1lll_opy_:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡅࡧࡶ࡯ࡹࡵࡰࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᓈ"))
                return False
            browser = caps.get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᓉ"), bstack11l1l11_opy_ (u"ࠩࠪᓊ")).lower()
            if browser != bstack11l1l11_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᓋ"):
                self.logger.warning(bstack11l1l11_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢᓌ"))
                return False
            bstack1l111ll111l_opy_ = bstack1l1111lllll_opy_
            if not self.config.get(bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᓍ")) or self.config.get(bstack11l1l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᓎ")):
                bstack1l111ll111l_opy_ = bstack1l111l1l1ll_opy_
            browser_version = caps.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᓏ"))
            if not browser_version:
                browser_version = caps.get(bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᓐ"), {}).get(bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᓑ"), bstack11l1l11_opy_ (u"ࠪࠫᓒ"))
            if browser_version and browser_version != bstack11l1l11_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫᓓ") and int(browser_version.split(bstack11l1l11_opy_ (u"ࠬ࠴ࠧᓔ"))[0]) <= bstack1l111ll111l_opy_:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࠣᓕ") + str(bstack1l111ll111l_opy_) + bstack11l1l11_opy_ (u"ࠢ࠯ࠤᓖ"))
                return False
            bstack1l111l1111l_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᓗ"), {}).get(bstack11l1l11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᓘ"))
            if not bstack1l111l1111l_opy_:
                bstack1l111l1111l_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᓙ"), {})
            if bstack1l111l1111l_opy_ and bstack11l1l11_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨᓚ") in bstack1l111l1111l_opy_.get(bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡵࠪᓛ"), []):
                self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣᓜ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡢ࡮࡬ࡨࡦࡺࡥࠡࡣ࠴࠵ࡾࠦࡳࡶࡲࡳࡳࡷࡺࠠ࠻ࠤᓝ") + str(error))
            return False
    def bstack1l111l11l11_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l1111ll111_opy_ = {
            bstack11l1l11_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨᓞ"): test_uuid,
        }
        bstack1l111l1ll1l_opy_ = {}
        if result.success:
            bstack1l111l1ll1l_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l1111llll1_opy_(bstack1l1111ll111_opy_, bstack1l111l1ll1l_opy_)
    def bstack1111l111_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1l11llll_opy_ = None
        try:
            self.bstack1lllll1l111_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11l1l11_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᓟ")
            req.script_name = bstack11l1l11_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣᓠ")
            r = self.bstack1llllllll11_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡤࡳ࡫ࡹࡩࡷࠦࡥࡹࡧࡦࡹࡹ࡫ࠠࡱࡣࡵࡥࡲࡹࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᓡ") + str(r.error) + bstack11l1l11_opy_ (u"ࠧࠨᓢ"))
            else:
                bstack1l1111ll111_opy_ = self.bstack1l111l11l11_opy_(test_uuid, r)
                bstack1lll1lll111_opy_ = r.script
            self.logger.debug(bstack11l1l11_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᓣ") + str(bstack1l1111ll111_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1lll111_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᓤ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠣࠢࠥᓥ"))
                return
            bstack1ll1l11llll_opy_ = bstack1llllll1ll1_opy_.bstack1ll1l11l111_opy_(EVENTS.bstack1l111l1l111_opy_.value)
            self.bstack1l1111l11ll_opy_(driver, bstack1lll1lll111_opy_, bstack1l1111ll111_opy_, framework_name)
            self.logger.info(bstack11l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧᓦ"))
            bstack1llllll1ll1_opy_.end(EVENTS.bstack1l111l1l111_opy_.value, bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᓧ"), bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᓨ"), True, None, command=bstack11l1l11_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᓩ"),test_name=name)
        except Exception as bstack1l11111ll11_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᓪ") + bstack11l1l11_opy_ (u"ࠢࡴࡶࡵࠬࡵࡧࡴࡩࠫࠥᓫ") + bstack11l1l11_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥᓬ") + str(bstack1l11111ll11_opy_))
            bstack1llllll1ll1_opy_.end(EVENTS.bstack1l111l1l111_opy_.value, bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᓭ"), bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᓮ"), False, bstack1l11111ll11_opy_, command=bstack11l1l11_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᓯ"),test_name=name)
    def bstack1l1111l11ll_opy_(self, driver, bstack1lll1lll111_opy_, bstack1l1111ll111_opy_, framework_name):
        if framework_name == bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᓰ"):
            self.bstack1l11l1l1111_opy_.bstack1llll1111l1_opy_(driver, bstack1lll1lll111_opy_, bstack1l1111ll111_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1lll111_opy_, bstack1l1111ll111_opy_))
    def _1l1111ll1ll_opy_(self, instance: bstack1lll1l1ll11_opy_, args: Tuple) -> list:
        bstack11l1l11_opy_ (u"ࠨࠢࠣࡇࡻࡸࡷࡧࡣࡵࠢࡷࡥ࡬ࡹࠠࡣࡣࡶࡩࡩࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࠣࠤࠥᓱ")
        if bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᓲ") in instance.bstack1l1lll1ll11_opy_:
            return args[2].tags if hasattr(args[2], bstack11l1l11_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᓳ")) else []
        if hasattr(args[0], bstack11l1l11_opy_ (u"ࠩࡲࡻࡳࡥ࡭ࡢࡴ࡮ࡩࡷࡹࠧᓴ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111l11111_opy_(self, tags, capabilities):
        return self.bstack1l111lll11_opy_(tags) and self.bstack1ll1l1ll1_opy_(capabilities)