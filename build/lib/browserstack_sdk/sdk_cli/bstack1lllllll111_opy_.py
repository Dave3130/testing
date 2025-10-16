# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack1lll111llll_opy_,
    bstack111111l111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_, bstack1llll1l1l11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l11l_opy_ import bstack1lll1l1lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1llll11l1l1_opy_
from bstack_utils.helper import bstack1l111l1l1ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
import grpc
import traceback
import json
class bstack1l1l11ll1l1_opy_(bstack1llll1llll1_opy_):
    bstack1l1ll1l1l1l_opy_ = False
    bstack1l111lll11l_opy_ = bstack1l_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵࠦᐴ")
    bstack1l111lllll1_opy_ = bstack1l_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࠥᐵ")
    bstack1l111l1l111_opy_ = bstack1l_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠ࡫ࡱ࡭ࡹࠨᐶ")
    bstack1l1111lllll_opy_ = bstack1l_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡ࡬ࡷࡤࡹࡣࡢࡰࡱ࡭ࡳ࡭ࠢᐷ")
    bstack1l111ll1lll_opy_ = bstack1l_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴࡢ࡬ࡦࡹ࡟ࡶࡴ࡯ࠦᐸ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l11l1lll_opy_, bstack1ll1llll1l1_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111l11l1l_opy_ = False
        self.bstack1l111l1ll1l_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l11ll1l_opy_ = bstack1ll1llll1l1_opy_
        bstack1l1l11l1lll_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1l111l1l1l1_opy_)
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.PRE), self.bstack1lll1lll1ll_opy_)
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111llll1_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        if self.bstack1l111l11l1l_opy_:
            self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᐹ")] = f.get_state(instance, TestFramework.bstack1llll11ll11_opy_)
        if bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩᐺ") in instance.bstack1ll11l1llll_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llll1lllll_opy_)
            self.accessibility = self.bstack1l111l111ll_opy_(tags, self.config[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᐻ")][platform_index])
        else:
            capabilities = self.bstack1l11l11ll1l_opy_.bstack1lll1l111ll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᐼ") + str(kwargs) + bstack1l_opy_ (u"ࠣࠤᐽ"))
                return
            self.accessibility = self.bstack1l111l111ll_opy_(tags, capabilities)
        if self.bstack1l11l11ll1l_opy_.pages and self.bstack1l11l11ll1l_opy_.pages.values():
            bstack1l111l1ll11_opy_ = list(self.bstack1l11l11ll1l_opy_.pages.values())
            if bstack1l111l1ll11_opy_ and isinstance(bstack1l111l1ll11_opy_[0], (list, tuple)) and bstack1l111l1ll11_opy_[0]:
                bstack1l111ll1l1l_opy_ = bstack1l111l1ll11_opy_[0][0]
                if callable(bstack1l111ll1l1l_opy_):
                    page = bstack1l111ll1l1l_opy_()
                    def bstack1l1l1llll_opy_():
                        self.get_accessibility_results(page, bstack1l_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᐾ"))
                    def bstack1l111l11111_opy_():
                        self.get_accessibility_results_summary(page, bstack1l_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᐿ"))
                    setattr(page, bstack1l_opy_ (u"ࠦ࡬࡫ࡴࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡒࡦࡵࡸࡰࡹࡹࠢᑀ"), bstack1l1l1llll_opy_)
                    setattr(page, bstack1l_opy_ (u"ࠧ࡭ࡥࡵࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡓࡧࡶࡹࡱࡺࡓࡶ࡯ࡰࡥࡷࡿࠢᑁ"), bstack1l111l11111_opy_)
        self.logger.debug(bstack1l_opy_ (u"ࠨࡳࡩࡱࡸࡰࡩࠦࡲࡶࡰࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡺࡦࡲࡵࡦ࠿ࠥᑂ") + str(self.accessibility) + bstack1l_opy_ (u"ࠢࠣᑃ"))
    def bstack1l111l1l1l1_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1l1111lll_opy_ = datetime.now()
            self.bstack1l111l11ll1_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡩ࡯࡫ࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡨࡵ࡮ࡧ࡫ࡪࠦᑄ"), datetime.now() - bstack1l1111lll_opy_)
            if (
                not f.bstack1l1lll11lll_opy_(method_name)
                or f.bstack1l1llll111l_opy_(method_name, *args)
                or f.bstack1l1lll1111l_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l11ll1l1_opy_.bstack1l111l1l111_opy_, False):
                if not bstack1l1l11ll1l1_opy_.bstack1l1ll1l1l1l_opy_:
                    self.logger.warning(bstack1l_opy_ (u"ࠤ࡞ࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࠧᑅ") + str(f.platform_index) + bstack1l_opy_ (u"ࠥࡡࠥࡧ࠱࠲ࡻࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢ࡫ࡥࡻ࡫ࠠ࡯ࡱࡷࠤࡧ࡫ࡥ࡯ࠢࡶࡩࡹࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᑆ"))
                    bstack1l1l11ll1l1_opy_.bstack1l1ll1l1l1l_opy_ = True
                return
            bstack1l111lll111_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111lll111_opy_:
                platform_index = f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_, 0)
                self.logger.debug(bstack1l_opy_ (u"ࠦࡳࡵࠠࡢ࠳࠴ࡽࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡰࡴࠣࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࢀࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᑇ") + str(f.framework_name) + bstack1l_opy_ (u"ࠧࠨᑈ"))
                return
            command_name = f.bstack1l1llll11l1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1l_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࠣᑉ") + str(method_name) + bstack1l_opy_ (u"ࠢࠣᑊ"))
                return
            bstack1l111l11l11_opy_ = f.get_state(instance, bstack1l1l11ll1l1_opy_.bstack1l111ll1lll_opy_, False)
            if command_name == bstack1l_opy_ (u"ࠣࡩࡨࡸࠧᑋ") and not bstack1l111l11l11_opy_:
                f.bstack1lllll11ll1_opy_(instance, bstack1l1l11ll1l1_opy_.bstack1l111ll1lll_opy_, True)
                bstack1l111l11l11_opy_ = True
            if not bstack1l111l11l11_opy_ and not self.bstack1l111l11l1l_opy_:
                self.logger.debug(bstack1l_opy_ (u"ࠤࡱࡳ࡛ࠥࡒࡍࠢ࡯ࡳࡦࡪࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑌ") + str(command_name) + bstack1l_opy_ (u"ࠥࠦᑍ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1l_opy_ (u"ࠦࡳࡵࠠࡢ࠳࠴ࡽࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤᑎ") + str(command_name) + bstack1l_opy_ (u"ࠧࠨᑏ"))
                return
            self.logger.info(bstack1l_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡼ࡮ࡨࡲ࠭ࡹࡣࡳ࡫ࡳࡸࡸࡥࡴࡰࡡࡵࡹࡳ࠯ࡽࠡࡵࡦࡶ࡮ࡶࡴࡴࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑐ") + str(command_name) + bstack1l_opy_ (u"ࠢࠣᑑ"))
            scripts = [(s, bstack1l111lll111_opy_[s]) for s in scripts_to_run if s in bstack1l111lll111_opy_]
            for script_name, bstack1lll1l11l11_opy_ in scripts:
                try:
                    bstack1l1111lll_opy_ = datetime.now()
                    if script_name == bstack1l_opy_ (u"ࠣࡵࡦࡥࡳࠨᑒ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࠣᑓ") + script_name, datetime.now() - bstack1l1111lll_opy_)
                    if isinstance(result, dict) and not result.get(bstack1l_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦᑔ"), True):
                        self.logger.warning(bstack1l_opy_ (u"ࠦࡸࡱࡩࡱࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡸࡥ࡮ࡣ࡬ࡲ࡮ࡴࡧࠡࡵࡦࡶ࡮ࡶࡴࡴ࠼ࠣࠦᑕ") + str(result) + bstack1l_opy_ (u"ࠧࠨᑖ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡵࡦࡶ࡮ࡶࡴ࠾ࡽࡶࡧࡷ࡯ࡰࡵࡡࡱࡥࡲ࡫ࡽࠡࡧࡵࡶࡴࡸ࠽ࠣᑗ") + str(e) + bstack1l_opy_ (u"ࠢࠣᑘ"))
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩࠥ࡫ࡲࡳࡱࡵࡁࠧᑙ") + str(e) + bstack1l_opy_ (u"ࠤࠥᑚ"))
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111llll1_opy_(instance, args)
        capabilities = self.bstack1l11l11ll1l_opy_.bstack1lll1l111ll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111l111ll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᑛ"))
            return
        driver = self.bstack1l11l11ll1l_opy_.bstack1lll1llll11_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll1l11lll1_opy_)
        if not test_name:
            self.logger.debug(bstack1l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᑜ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1llll11ll11_opy_)
        if not test_uuid:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥᑝ"))
            return
        if isinstance(self.bstack1l11l11ll1l_opy_, bstack1lll1l1lll1_opy_):
            framework_name = bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᑞ")
        else:
            framework_name = bstack1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩᑟ")
        self.bstack111l1ll1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1l111ll11_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1l_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࠤᑠ"))
            return
        bstack1l1111lll_opy_ = datetime.now()
        bstack1lll1l11l11_opy_ = self.scripts.get(framework_name, {}).get(bstack1l_opy_ (u"ࠤࡶࡧࡦࡴࠢᑡ"), None)
        if not bstack1lll1l11l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠬࡹࡣࡢࡰࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᑢ") + str(framework_name) + bstack1l_opy_ (u"ࠦࠥࠨᑣ"))
            return
        if self.bstack1l111l11l1l_opy_:
            arg = dict()
            arg[bstack1l_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᑤ")] = method if method else bstack1l_opy_ (u"ࠨࠢᑥ")
            arg[bstack1l_opy_ (u"ࠢࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠢᑦ")] = self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᑧ")]
            arg[bstack1l_opy_ (u"ࠤࡷ࡬ࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠢᑨ")] = self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠣᑩ")]
            arg[bstack1l_opy_ (u"ࠦࡦࡻࡴࡩࡊࡨࡥࡩ࡫ࡲࠣᑪ")] = self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠥᑫ")]
            arg[bstack1l_opy_ (u"ࠨࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠥᑬ")] = self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠢࡵࡪࡢ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳࠨᑭ")]
            arg[bstack1l_opy_ (u"ࠣࡵࡦࡥࡳ࡚ࡩ࡮ࡧࡶࡸࡦࡳࡰࠣᑮ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l1111ll1ll_opy_ = bstack1lll1l11l11_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l1111ll1ll_opy_)
            return
        instance = bstack1lll111llll_opy_.bstack1ll11ll1ll1_opy_(driver)
        if instance:
            if not bstack1lll111llll_opy_.get_state(instance, bstack1l1l11ll1l1_opy_.bstack1l1111lllll_opy_, False):
                bstack1lll111llll_opy_.bstack1lllll11ll1_opy_(instance, bstack1l1l11ll1l1_opy_.bstack1l1111lllll_opy_, True)
            else:
                self.logger.info(bstack1l_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡳࠦࡰࡳࡱࡪࡶࡪࡹࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨᑯ") + str(method) + bstack1l_opy_ (u"ࠥࠦᑰ"))
                return
        self.logger.info(bstack1l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤ࠾ࠤᑱ") + str(method) + bstack1l_opy_ (u"ࠧࠨᑲ"))
        if framework_name == bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᑳ"):
            result = self.bstack1l11l11ll1l_opy_.bstack1llll111l11_opy_(driver, bstack1lll1l11l11_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1l11l11_opy_, {bstack1l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᑴ"): method if method else bstack1l_opy_ (u"ࠣࠤᑵ")})
        bstack1llll1l1lll_opy_.end(EVENTS.bstack1l111ll11_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᑶ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᑷ"), True, None, command=method)
        if instance:
            bstack1lll111llll_opy_.bstack1lllll11ll1_opy_(instance, bstack1l1l11ll1l1_opy_.bstack1l1111lllll_opy_, False)
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮ࠣᑸ"), datetime.now() - bstack1l1111lll_opy_)
        return result
        def bstack1l111l1llll_opy_(self, driver: object, framework_name, bstack111lll1l11_opy_: str):
            self.bstack1lllll1l111_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111ll1l1_opy_ = self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᑹ")]
            req.bstack111lll1l11_opy_ = bstack111lll1l11_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llll1lll1l_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᑺ") + str(r) + bstack1l_opy_ (u"ࠢࠣᑻ"))
                else:
                    bstack1l111ll111l_opy_ = json.loads(r.bstack1l111ll1l11_opy_.decode(bstack1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᑼ")))
                    if bstack111lll1l11_opy_ == bstack1l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ᑽ"):
                        return bstack1l111ll111l_opy_.get(bstack1l_opy_ (u"ࠥࡨࡦࡺࡡࠣᑾ"), [])
                    else:
                        return bstack1l111ll111l_opy_.get(bstack1l_opy_ (u"ࠦࡩࡧࡴࡢࠤᑿ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡩࡹࡥࡡࡱࡲࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࠣࡪࡷࡵ࡭ࠡࡥ࡯࡭࠿ࠦࠢᒀ") + str(e) + bstack1l_opy_ (u"ࠨࠢᒁ"))
    @measure(event_name=EVENTS.bstack1l1l1lll1l_opy_, stage=STAGE.bstack11ll111111_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᒂ"))
            return
        if self.bstack1l111l11l1l_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡢࡲࡳࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᒃ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack1l_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᒄ"))
        bstack1lll1l11l11_opy_ = self.scripts.get(framework_name, {}).get(bstack1l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢᒅ"), None)
        if not bstack1lll1l11l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᒆ") + str(framework_name) + bstack1l_opy_ (u"ࠧࠨᒇ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l1111lll_opy_ = datetime.now()
        if framework_name == bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒈ"):
            result = self.bstack1l11l11ll1l_opy_.bstack1llll111l11_opy_(driver, bstack1lll1l11l11_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1l11l11_opy_)
        instance = bstack1lll111llll_opy_.bstack1ll11ll1ll1_opy_(driver)
        if instance:
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࠥᒉ"), datetime.now() - bstack1l1111lll_opy_)
        return result
    @measure(event_name=EVENTS.bstack11l1111l11_opy_, stage=STAGE.bstack11ll111111_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡥࡳࡶ࡯ࡰࡥࡷࡿ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᒊ"))
            return
        if self.bstack1l111l11l1l_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack1l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ᒋ"))
        bstack1lll1l11l11_opy_ = self.scripts.get(framework_name, {}).get(bstack1l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢᒌ"), None)
        if not bstack1lll1l11l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᒍ") + str(framework_name) + bstack1l_opy_ (u"ࠧࠨᒎ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l1111lll_opy_ = datetime.now()
        if framework_name == bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒏ"):
            result = self.bstack1l11l11ll1l_opy_.bstack1llll111l11_opy_(driver, bstack1lll1l11l11_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1l11l11_opy_)
        instance = bstack1lll111llll_opy_.bstack1ll11ll1ll1_opy_(driver)
        if instance:
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࡢࡷࡺࡳ࡭ࡢࡴࡼࠦᒐ"), datetime.now() - bstack1l1111lll_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111ll1111_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1l1111lll1l_opy_(
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
            r = self.bstack1llll1lll1l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᒑ") + str(r) + bstack1l_opy_ (u"ࠤࠥᒒ"))
            else:
                self.bstack1l111llll11_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᒓ") + str(e) + bstack1l_opy_ (u"ࠦࠧᒔ"))
            traceback.print_exc()
            raise e
    def bstack1l111llll11_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡲ࡯ࡢࡦࡢࡧࡴࡴࡦࡪࡩ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧᒕ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111l11l1l_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡣࡷ࡬ࡰࡩࡥࡵࡶ࡫ࡧࠦᒖ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111l1ll1l_opy_[bstack1l_opy_ (u"ࠢࡵࡪࡢ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳࠨᒗ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111l1ll1l_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111ll11ll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111lll11l_opy_ and command.module == self.bstack1l111lllll1_opy_:
                        if command.method and not command.method in bstack1l111ll11ll_opy_:
                            bstack1l111ll11ll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111ll11ll_opy_[command.method]:
                            bstack1l111ll11ll_opy_[command.method][command.name] = list()
                        bstack1l111ll11ll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111ll11ll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l11ll1_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        exec: Tuple[bstack111111l111_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l11ll1l_opy_, bstack1lll1l1lll1_opy_) and method_name != bstack1l_opy_ (u"ࠨࡥࡲࡲࡳ࡫ࡣࡵࠩᒘ"):
            return
        if bstack1lll111llll_opy_.bstack1llllllll11_opy_(instance, bstack1l1l11ll1l1_opy_.bstack1l111l1l111_opy_):
            return
        if f.bstack1lllll1llll_opy_(method_name, *args):
            bstack1l111ll11l1_opy_ = False
            desired_capabilities = f.bstack1l1lll1l1ll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1llll1ll1_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_, 0)
                bstack1l111l1lll1_opy_ = datetime.now()
                r = self.bstack1l1111lll1l_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡤࡱࡱࡪ࡮࡭ࠢᒙ"), datetime.now() - bstack1l111l1lll1_opy_)
                bstack1l111ll11l1_opy_ = r.success
            else:
                self.logger.error(bstack1l_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࡩ࡫ࡳࡪࡴࡨࡨࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࡁࠧᒚ") + str(desired_capabilities) + bstack1l_opy_ (u"ࠦࠧᒛ"))
            f.bstack1lllll11ll1_opy_(instance, bstack1l1l11ll1l1_opy_.bstack1l111l1l111_opy_, bstack1l111ll11l1_opy_)
    def bstack111l11l11_opy_(self, test_tags):
        bstack1l1111lll1l_opy_ = self.config.get(bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᒜ"))
        if not bstack1l1111lll1l_opy_:
            return True
        try:
            include_tags = bstack1l1111lll1l_opy_[bstack1l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒝ")] if bstack1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒞ") in bstack1l1111lll1l_opy_ and isinstance(bstack1l1111lll1l_opy_[bstack1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒟ")], list) else []
            exclude_tags = bstack1l1111lll1l_opy_[bstack1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒠ")] if bstack1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒡ") in bstack1l1111lll1l_opy_ and isinstance(bstack1l1111lll1l_opy_[bstack1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒢ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧᒣ") + str(error))
        return False
    def bstack1l1l11ll1l_opy_(self, caps):
        try:
            if self.bstack1l111l11l1l_opy_:
                bstack1l1111ll11l_opy_ = caps.get(bstack1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧᒤ"))
                if bstack1l1111ll11l_opy_ is not None and str(bstack1l1111ll11l_opy_).lower() == bstack1l_opy_ (u"ࠢࡢࡰࡧࡶࡴ࡯ࡤࠣᒥ"):
                    bstack1l111llll1l_opy_ = caps.get(bstack1l_opy_ (u"ࠣࡣࡳࡴ࡮ࡻ࡭࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᒦ")) or caps.get(bstack1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᒧ"))
                    if bstack1l111llll1l_opy_ is not None and int(bstack1l111llll1l_opy_) < 11:
                        self.logger.warning(bstack1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡅࡳࡪࡲࡰ࡫ࡧࠤ࠶࠷ࠠࡢࡰࡧࠤࡦࡨ࡯ࡷࡧ࠱ࠤࡈࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡ࠿ࠥᒨ") + str(bstack1l111llll1l_opy_) + bstack1l_opy_ (u"ࠦࠧᒩ"))
                        return False
                return True
            bstack1l111llllll_opy_ = caps.get(bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᒪ"), {}).get(bstack1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪᒫ"), caps.get(bstack1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧᒬ"), bstack1l_opy_ (u"ࠨࠩᒭ")))
            if bstack1l111llllll_opy_:
                self.logger.warning(bstack1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᒮ"))
                return False
            browser = caps.get(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᒯ"), bstack1l_opy_ (u"ࠫࠬᒰ")).lower()
            if browser != bstack1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᒱ"):
                self.logger.warning(bstack1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤᒲ"))
                return False
            bstack1l111l11lll_opy_ = bstack1l111ll1ll1_opy_
            if not self.config.get(bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᒳ")) or self.config.get(bstack1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᒴ")):
                bstack1l111l11lll_opy_ = bstack1l1111lll11_opy_
            browser_version = caps.get(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᒵ"))
            if not browser_version:
                browser_version = caps.get(bstack1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᒶ"), {}).get(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᒷ"), bstack1l_opy_ (u"ࠬ࠭ᒸ"))
            if browser_version and browser_version != bstack1l_opy_ (u"࠭࡬ࡢࡶࡨࡷࡹ࠭ᒹ") and int(browser_version.split(bstack1l_opy_ (u"ࠧ࠯ࠩᒺ"))[0]) <= bstack1l111l11lll_opy_:
                self.logger.warning(bstack1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠣ࡫ࡷ࡫ࡡࡵࡧࡵࠤࡹ࡮ࡡ࡯ࠢࠥᒻ") + str(bstack1l111l11lll_opy_) + bstack1l_opy_ (u"ࠤ࠱ࠦᒼ"))
                return False
            bstack1l111lll1l1_opy_ = caps.get(bstack1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᒽ"), {}).get(bstack1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᒾ"))
            if not bstack1l111lll1l1_opy_:
                bstack1l111lll1l1_opy_ = caps.get(bstack1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᒿ"), {})
            if bstack1l111lll1l1_opy_ and bstack1l_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪᓀ") in bstack1l111lll1l1_opy_.get(bstack1l_opy_ (u"ࠧࡢࡴࡪࡷࠬᓁ"), []):
                self.logger.warning(bstack1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥᓂ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦᓃ") + str(error))
            return False
    def bstack1l111lll1ll_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l111l1_opy_ = {
            bstack1l_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪᓄ"): test_uuid,
        }
        bstack1l11l111111_opy_ = {}
        if result.success:
            bstack1l11l111111_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l1l1ll_opy_(bstack1l111l111l1_opy_, bstack1l11l111111_opy_)
    def bstack111l1ll1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1l1lll11_opy_ = None
        try:
            self.bstack1lllll1l111_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1l_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦᓅ")
            req.script_name = bstack1l_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥᓆ")
            r = self.bstack1llll1lll1l_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡧࡻࡩࡨࡻࡴࡦࠢࡳࡥࡷࡧ࡭ࡴࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᓇ") + str(r.error) + bstack1l_opy_ (u"ࠢࠣᓈ"))
            else:
                bstack1l111l111l1_opy_ = self.bstack1l111lll1ll_opy_(test_uuid, r)
                bstack1lll1l11l11_opy_ = r.script
            self.logger.debug(bstack1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡦࡼࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫᓉ") + str(bstack1l111l111l1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1l11l11_opy_:
                self.logger.debug(bstack1l_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᓊ") + str(framework_name) + bstack1l_opy_ (u"ࠥࠤࠧᓋ"))
                return
            bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1l111l1111l_opy_.value)
            self.bstack1l111l1l11l_opy_(driver, bstack1lll1l11l11_opy_, bstack1l111l111l1_opy_, framework_name)
            self.logger.info(bstack1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠢᓌ"))
            bstack1llll1l1lll_opy_.end(EVENTS.bstack1l111l1111l_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᓍ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᓎ"), True, None, command=bstack1l_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬᓏ"),test_name=name)
        except Exception as bstack1l1111ll111_opy_:
            self.logger.error(bstack1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥᓐ") + bstack1l_opy_ (u"ࠤࡶࡸࡷ࠮ࡰࡢࡶ࡫࠭ࠧᓑ") + bstack1l_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧᓒ") + str(bstack1l1111ll111_opy_))
            bstack1llll1l1lll_opy_.end(EVENTS.bstack1l111l1111l_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᓓ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᓔ"), False, bstack1l1111ll111_opy_, command=bstack1l_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᓕ"),test_name=name)
    def bstack1l111l1l11l_opy_(self, driver, bstack1lll1l11l11_opy_, bstack1l111l111l1_opy_, framework_name):
        if framework_name == bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᓖ"):
            self.bstack1l11l11ll1l_opy_.bstack1llll111l11_opy_(driver, bstack1lll1l11l11_opy_, bstack1l111l111l1_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1l11l11_opy_, bstack1l111l111l1_opy_))
    def _1l1111llll1_opy_(self, instance: bstack1llll1l1l11_opy_, args: Tuple) -> list:
        bstack1l_opy_ (u"ࠣࠤࠥࡉࡽࡺࡲࡢࡥࡷࠤࡹࡧࡧࡴࠢࡥࡥࡸ࡫ࡤࠡࡱࡱࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࠥࠦࠧᓗ")
        if bstack1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᓘ") in instance.bstack1ll11l1llll_opy_:
            return args[2].tags if hasattr(args[2], bstack1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᓙ")) else []
        if hasattr(args[0], bstack1l_opy_ (u"ࠫࡴࡽ࡮ࡠ࡯ࡤࡶࡰ࡫ࡲࡴࠩᓚ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111l111ll_opy_(self, tags, capabilities):
        return self.bstack111l11l11_opy_(tags) and self.bstack1l1l11ll1l_opy_(capabilities)