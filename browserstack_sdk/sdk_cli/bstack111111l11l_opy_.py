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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lll111ll1l_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111lll_opy_, bstack1lll1lll11l_opy_, bstack1lll1lll1l1_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll11_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1llll11llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1llll11l1ll_opy_
from bstack_utils.helper import bstack1l111l1ll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
import grpc
import traceback
import json
class bstack1l1l11lllll_opy_(bstack1llllll111l_opy_):
    bstack1l1ll1l1l1l_opy_ = False
    bstack1l111l1ll11_opy_ = bstack111111l_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶࠧᐧ")
    bstack1l1111ll11l_opy_ = bstack111111l_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥ࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵࠦᐨ")
    bstack1l111l11lll_opy_ = bstack111111l_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡ࡬ࡲ࡮ࡺࠢᐩ")
    bstack1l111ll1111_opy_ = bstack111111l_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢ࡭ࡸࡥࡳࡤࡣࡱࡲ࡮ࡴࡧࠣᐪ")
    bstack1l1111lllll_opy_ = bstack111111l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵࡣ࡭ࡧࡳࡠࡷࡵࡰࠧᐫ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l11l1lll_opy_, bstack1ll1lllll11_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111l1l1ll_opy_ = False
        self.bstack1l1111lll11_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11ll11lll_opy_ = bstack1ll1lllll11_opy_
        bstack1l1l11l1lll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1l1111llll1_opy_)
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1lll1ll1lll_opy_)
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll11l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l1l1l1_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        if self.bstack1l111l1l1ll_opy_:
            self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᐬ")] = f.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        if bstack111111l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᐭ") in instance.bstack1ll11l11ll1_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llllllll1l_opy_)
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, self.config[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᐮ")][platform_index])
        else:
            capabilities = self.bstack1l11ll11lll_opy_.bstack1lll1llll1l_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack111111l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᐯ") + str(kwargs) + bstack111111l_opy_ (u"ࠤࠥᐰ"))
                return
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if self.bstack1l11ll11lll_opy_.pages and self.bstack1l11ll11lll_opy_.pages.values():
            bstack1l111l11l11_opy_ = list(self.bstack1l11ll11lll_opy_.pages.values())
            if bstack1l111l11l11_opy_ and isinstance(bstack1l111l11l11_opy_[0], (list, tuple)) and bstack1l111l11l11_opy_[0]:
                bstack1l111l1lll1_opy_ = bstack1l111l11l11_opy_[0][0]
                if callable(bstack1l111l1lll1_opy_):
                    page = bstack1l111l1lll1_opy_()
                    def bstack1ll111ll11_opy_():
                        self.get_accessibility_results(page, bstack111111l_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᐱ"))
                    def bstack1l111lll111_opy_():
                        self.get_accessibility_results_summary(page, bstack111111l_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᐲ"))
                    setattr(page, bstack111111l_opy_ (u"ࠧ࡭ࡥࡵࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡓࡧࡶࡹࡱࡺࡳࠣᐳ"), bstack1ll111ll11_opy_)
                    setattr(page, bstack111111l_opy_ (u"ࠨࡧࡦࡶࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡔࡨࡷࡺࡲࡴࡔࡷࡰࡱࡦࡸࡹࠣᐴ"), bstack1l111lll111_opy_)
        self.logger.debug(bstack111111l_opy_ (u"ࠢࡴࡪࡲࡹࡱࡪࠠࡳࡷࡱࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡻࡧ࡬ࡶࡧࡀࠦᐵ") + str(self.accessibility) + bstack111111l_opy_ (u"ࠣࠤᐶ"))
    def bstack1l1111llll1_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1111ll111_opy_ = datetime.now()
            self.bstack1l111llll1l_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡪࡰ࡬ࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡩ࡯࡯ࡨ࡬࡫ࠧᐷ"), datetime.now() - bstack1111ll111_opy_)
            if (
                not f.bstack1l1lll111l1_opy_(method_name)
                or f.bstack1l1lll1l1ll_opy_(method_name, *args)
                or f.bstack1l1llll1l11_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l11lllll_opy_.bstack1l111l11lll_opy_, False):
                if not bstack1l1l11lllll_opy_.bstack1l1ll1l1l1l_opy_:
                    self.logger.warning(bstack111111l_opy_ (u"ࠥ࡟ࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࠨᐸ") + str(f.platform_index) + bstack111111l_opy_ (u"ࠦࡢࠦࡡ࠲࠳ࡼࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣ࡬ࡦࡼࡥࠡࡰࡲࡸࠥࡨࡥࡦࡰࠣࡷࡪࡺࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡶࡩࡸࡹࡩࡰࡰࠥᐹ"))
                    bstack1l1l11lllll_opy_.bstack1l1ll1l1l1l_opy_ = True
                return
            bstack1l111ll11l1_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111ll11l1_opy_:
                platform_index = f.get_state(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_, 0)
                self.logger.debug(bstack111111l_opy_ (u"ࠧࡴ࡯ࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡱࡵࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᐺ") + str(f.framework_name) + bstack111111l_opy_ (u"ࠨࠢᐻ"))
                return
            command_name = f.bstack1l1llll11l1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack111111l_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࠤᐼ") + str(method_name) + bstack111111l_opy_ (u"ࠣࠤᐽ"))
                return
            bstack1l111l1111l_opy_ = f.get_state(instance, bstack1l1l11lllll_opy_.bstack1l1111lllll_opy_, False)
            if command_name == bstack111111l_opy_ (u"ࠤࡪࡩࡹࠨᐾ") and not bstack1l111l1111l_opy_:
                f.bstack1llll1lll1l_opy_(instance, bstack1l1l11lllll_opy_.bstack1l1111lllll_opy_, True)
                bstack1l111l1111l_opy_ = True
            if not bstack1l111l1111l_opy_ and not self.bstack1l111l1l1ll_opy_:
                self.logger.debug(bstack111111l_opy_ (u"ࠥࡲࡴࠦࡕࡓࡎࠣࡰࡴࡧࡤࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤᐿ") + str(command_name) + bstack111111l_opy_ (u"ࠦࠧᑀ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack111111l_opy_ (u"ࠧࡴ࡯ࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᑁ") + str(command_name) + bstack111111l_opy_ (u"ࠨࠢᑂ"))
                return
            self.logger.info(bstack111111l_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠡࡽ࡯ࡩࡳ࠮ࡳࡤࡴ࡬ࡴࡹࡹ࡟ࡵࡱࡢࡶࡺࡴࠩࡾࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤᑃ") + str(command_name) + bstack111111l_opy_ (u"ࠣࠤᑄ"))
            scripts = [(s, bstack1l111ll11l1_opy_[s]) for s in scripts_to_run if s in bstack1l111ll11l1_opy_]
            for script_name, bstack1lll1ll1111_opy_ in scripts:
                try:
                    bstack1111ll111_opy_ = datetime.now()
                    if script_name == bstack111111l_opy_ (u"ࠤࡶࡧࡦࡴࠢᑅ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࠤᑆ") + script_name, datetime.now() - bstack1111ll111_opy_)
                    if isinstance(result, dict) and not result.get(bstack111111l_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧᑇ"), True):
                        self.logger.warning(bstack111111l_opy_ (u"ࠧࡹ࡫ࡪࡲࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡲࡦ࡯ࡤ࡭ࡳ࡯࡮ࡨࠢࡶࡧࡷ࡯ࡰࡵࡵ࠽ࠤࠧᑈ") + str(result) + bstack111111l_opy_ (u"ࠨࠢᑉ"))
                        break
                except Exception as e:
                    self.logger.error(bstack111111l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡶࡧࡷ࡯ࡰࡵ࠿ࡾࡷࡨࡸࡩࡱࡶࡢࡲࡦࡳࡥࡾࠢࡨࡶࡷࡵࡲ࠾ࠤᑊ") + str(e) + bstack111111l_opy_ (u"ࠣࠤᑋ"))
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࠦࡥࡳࡴࡲࡶࡂࠨᑌ") + str(e) + bstack111111l_opy_ (u"ࠥࠦᑍ"))
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l1l1l1_opy_(instance, args)
        capabilities = self.bstack1l11ll11lll_opy_.bstack1lll1llll1l_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᑎ"))
            return
        driver = self.bstack1l11ll11lll_opy_.bstack1llll1111ll_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11lll111_opy_)
        if not test_name:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᑏ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        if not test_uuid:
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᑐ"))
            return
        if isinstance(self.bstack1l11ll11lll_opy_, bstack1llll11llll_opy_):
            framework_name = bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᑑ")
        else:
            framework_name = bstack111111l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪᑒ")
        self.bstack1lllllll1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack11lll1llll_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࠥᑓ"))
            return
        bstack1111ll111_opy_ = datetime.now()
        bstack1lll1ll1111_opy_ = self.scripts.get(framework_name, {}).get(bstack111111l_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᑔ"), None)
        if not bstack1lll1ll1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡳࡤࡣࡱࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᑕ") + str(framework_name) + bstack111111l_opy_ (u"ࠧࠦࠢᑖ"))
            return
        if self.bstack1l111l1l1ll_opy_:
            arg = dict()
            arg[bstack111111l_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨᑗ")] = method if method else bstack111111l_opy_ (u"ࠢࠣᑘ")
            arg[bstack111111l_opy_ (u"ࠣࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠣᑙ")] = self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᑚ")]
            arg[bstack111111l_opy_ (u"ࠥࡸ࡭ࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠣᑛ")] = self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠤᑜ")]
            arg[bstack111111l_opy_ (u"ࠧࡧࡵࡵࡪࡋࡩࡦࡪࡥࡳࠤᑝ")] = self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠦᑞ")]
            arg[bstack111111l_opy_ (u"ࠢࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠦᑟ")] = self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠣࡶ࡫ࡣ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠢᑠ")]
            arg[bstack111111l_opy_ (u"ࠤࡶࡧࡦࡴࡔࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠤᑡ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111l11111_opy_ = bstack1lll1ll1111_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l11111_opy_)
            return
        instance = bstack1lll111ll1l_opy_.bstack1ll11ll1lll_opy_(driver)
        if instance:
            if not bstack1lll111ll1l_opy_.get_state(instance, bstack1l1l11lllll_opy_.bstack1l111ll1111_opy_, False):
                bstack1lll111ll1l_opy_.bstack1llll1lll1l_opy_(instance, bstack1l1l11lllll_opy_.bstack1l111ll1111_opy_, True)
            else:
                self.logger.info(bstack111111l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡮ࡴࠠࡱࡴࡲ࡫ࡷ࡫ࡳࡴࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡃࠢᑢ") + str(method) + bstack111111l_opy_ (u"ࠦࠧᑣ"))
                return
        self.logger.info(bstack111111l_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥ࠿ࠥᑤ") + str(method) + bstack111111l_opy_ (u"ࠨࠢᑥ"))
        if framework_name == bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᑦ"):
            result = self.bstack1l11ll11lll_opy_.bstack1llll11l11l_opy_(driver, bstack1lll1ll1111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll1111_opy_, {bstack111111l_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠣᑧ"): method if method else bstack111111l_opy_ (u"ࠤࠥᑨ")})
        bstack1llllll1lll_opy_.end(EVENTS.bstack11lll1llll_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᑩ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᑪ"), True, None, command=method)
        if instance:
            bstack1lll111ll1l_opy_.bstack1llll1lll1l_opy_(instance, bstack1l1l11lllll_opy_.bstack1l111ll1111_opy_, False)
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽ࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯ࠤᑫ"), datetime.now() - bstack1111ll111_opy_)
        return result
        def bstack1l111l1llll_opy_(self, driver: object, framework_name, bstack1111ll11l_opy_: str):
            self.bstack1llll1l1ll1_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l111lll11l_opy_ = self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩࠨᑬ")]
            req.bstack1111ll11l_opy_ = bstack1111ll11l_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack111111111l_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack111111l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᑭ") + str(r) + bstack111111l_opy_ (u"ࠣࠤᑮ"))
                else:
                    bstack1l111l111ll_opy_ = json.loads(r.bstack1l111ll1l11_opy_.decode(bstack111111l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᑯ")))
                    if bstack1111ll11l_opy_ == bstack111111l_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧᑰ"):
                        return bstack1l111l111ll_opy_.get(bstack111111l_opy_ (u"ࠦࡩࡧࡴࡢࠤᑱ"), [])
                    else:
                        return bstack1l111l111ll_opy_.get(bstack111111l_opy_ (u"ࠧࡪࡡࡵࡣࠥᑲ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack111111l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡪࡺ࡟ࡢࡲࡳࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࠤ࡫ࡸ࡯࡮ࠢࡦࡰ࡮ࡀࠠࠣᑳ") + str(e) + bstack111111l_opy_ (u"ࠢࠣᑴ"))
    @measure(event_name=EVENTS.bstack1ll11l1lll_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥᑵ"))
            return
        if self.bstack1l111l1l1ll_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤ࡫ࡵࡲࠡࡣࡳࡴࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᑶ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack111111l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢᑷ"))
        bstack1lll1ll1111_opy_ = self.scripts.get(framework_name, {}).get(bstack111111l_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠣᑸ"), None)
        if not bstack1lll1ll1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᑹ") + str(framework_name) + bstack111111l_opy_ (u"ࠨࠢᑺ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1111ll111_opy_ = datetime.now()
        if framework_name == bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᑻ"):
            result = self.bstack1l11ll11lll_opy_.bstack1llll11l11l_opy_(driver, bstack1lll1ll1111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll1111_opy_)
        instance = bstack1lll111ll1l_opy_.bstack1ll11ll1lll_opy_(driver)
        if instance:
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࠦᑼ"), datetime.now() - bstack1111ll111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1llll11111_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹ࡟ࡴࡷࡰࡱࡦࡸࡹ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧᑽ"))
            return
        if self.bstack1l111l1l1ll_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack111111l_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧᑾ"))
        bstack1lll1ll1111_opy_ = self.scripts.get(framework_name, {}).get(bstack111111l_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣᑿ"), None)
        if not bstack1lll1ll1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᒀ") + str(framework_name) + bstack111111l_opy_ (u"ࠨࠢᒁ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1111ll111_opy_ = datetime.now()
        if framework_name == bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᒂ"):
            result = self.bstack1l11ll11lll_opy_.bstack1llll11l11l_opy_(driver, bstack1lll1ll1111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll1111_opy_)
        instance = bstack1lll111ll1l_opy_.bstack1ll11ll1lll_opy_(driver)
        if instance:
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࡣࡸࡻ࡭࡮ࡣࡵࡽࠧᒃ"), datetime.now() - bstack1111ll111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111ll111l_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1l111l11ll1_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llll1l1ll1_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack111111111l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack111111l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᒄ") + str(r) + bstack111111l_opy_ (u"ࠥࠦᒅ"))
            else:
                self.bstack1l1111ll1l1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᒆ") + str(e) + bstack111111l_opy_ (u"ࠧࠨᒇ"))
            traceback.print_exc()
            raise e
    def bstack1l1111ll1l1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡬ࡰࡣࡧࡣࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨᒈ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111l1l1ll_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠢࡵࡧࡶࡸ࡭ࡻࡢࡠࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠧᒉ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l1111lll11_opy_[bstack111111l_opy_ (u"ࠣࡶ࡫ࡣ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠢᒊ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l1111lll11_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111ll1lll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111l1ll11_opy_ and command.module == self.bstack1l1111ll11l_opy_:
                        if command.method and not command.method in bstack1l111ll1lll_opy_:
                            bstack1l111ll1lll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111ll1lll_opy_[command.method]:
                            bstack1l111ll1lll_opy_[command.method][command.name] = list()
                        bstack1l111ll1lll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111ll1lll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111llll1l_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11ll11lll_opy_, bstack1llll11llll_opy_) and method_name != bstack111111l_opy_ (u"ࠩࡦࡳࡳࡴࡥࡤࡶࠪᒋ"):
            return
        if bstack1lll111ll1l_opy_.bstack1lllllll11l_opy_(instance, bstack1l1l11lllll_opy_.bstack1l111l11lll_opy_):
            return
        if f.bstack1llllllllll_opy_(method_name, *args):
            bstack1l111lll1l1_opy_ = False
            desired_capabilities = f.bstack1l1lll11l1l_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1llll11ll_opy_(instance)
                platform_index = f.get_state(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_, 0)
                bstack1l111l111l1_opy_ = datetime.now()
                r = self.bstack1l111l11ll1_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡥࡲࡲ࡫࡯ࡧࠣᒌ"), datetime.now() - bstack1l111l111l1_opy_)
                bstack1l111lll1l1_opy_ = r.success
            else:
                self.logger.error(bstack111111l_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡪࡥࡴ࡫ࡵࡩࡩࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࡂࠨᒍ") + str(desired_capabilities) + bstack111111l_opy_ (u"ࠧࠨᒎ"))
            f.bstack1llll1lll1l_opy_(instance, bstack1l1l11lllll_opy_.bstack1l111l11lll_opy_, bstack1l111lll1l1_opy_)
    def bstack11l11ll11l_opy_(self, test_tags):
        bstack1l111l11ll1_opy_ = self.config.get(bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᒏ"))
        if not bstack1l111l11ll1_opy_:
            return True
        try:
            include_tags = bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒐ")] if bstack111111l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒑ") in bstack1l111l11ll1_opy_ and isinstance(bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒒ")], list) else []
            exclude_tags = bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒓ")] if bstack111111l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒔ") in bstack1l111l11ll1_opy_ and isinstance(bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒕ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack111111l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨᒖ") + str(error))
        return False
    def bstack1l1l1ll11_opy_(self, caps):
        try:
            if self.bstack1l111l1l1ll_opy_:
                bstack1l111lll1ll_opy_ = caps.get(bstack111111l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨᒗ"))
                if bstack1l111lll1ll_opy_ is not None and str(bstack1l111lll1ll_opy_).lower() == bstack111111l_opy_ (u"ࠣࡣࡱࡨࡷࡵࡩࡥࠤᒘ"):
                    bstack1l111l1l11l_opy_ = caps.get(bstack111111l_opy_ (u"ࠤࡤࡴࡵ࡯ࡵ࡮࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᒙ")) or caps.get(bstack111111l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧᒚ"))
                    if bstack1l111l1l11l_opy_ is not None and int(bstack1l111l1l11l_opy_) < 11:
                        self.logger.warning(bstack111111l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡆࡴࡤࡳࡱ࡬ࡨࠥ࠷࠱ࠡࡣࡱࡨࠥࡧࡢࡰࡸࡨ࠲ࠥࡉࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡀࠦᒛ") + str(bstack1l111l1l11l_opy_) + bstack111111l_opy_ (u"ࠧࠨᒜ"))
                        return False
                return True
            bstack1l1111ll1ll_opy_ = caps.get(bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᒝ"), {}).get(bstack111111l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᒞ"), caps.get(bstack111111l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨᒟ"), bstack111111l_opy_ (u"ࠩࠪᒠ")))
            if bstack1l1111ll1ll_opy_:
                self.logger.warning(bstack111111l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡈࡪࡹ࡫ࡵࡱࡳࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢᒡ"))
                return False
            browser = caps.get(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᒢ"), bstack111111l_opy_ (u"ࠬ࠭ᒣ")).lower()
            if browser != bstack111111l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ᒤ"):
                self.logger.warning(bstack111111l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥᒥ"))
                return False
            bstack1l1111l1ll1_opy_ = bstack1l111l11l1l_opy_
            if not self.config.get(bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᒦ")) or self.config.get(bstack111111l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᒧ")):
                bstack1l1111l1ll1_opy_ = bstack1l111lllll1_opy_
            browser_version = caps.get(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᒨ"))
            if not browser_version:
                browser_version = caps.get(bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᒩ"), {}).get(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᒪ"), bstack111111l_opy_ (u"࠭ࠧᒫ"))
            if browser_version and browser_version != bstack111111l_opy_ (u"ࠧ࡭ࡣࡷࡩࡸࡺࠧᒬ") and int(browser_version.split(bstack111111l_opy_ (u"ࠨ࠰ࠪᒭ"))[0]) <= bstack1l1111l1ll1_opy_:
                self.logger.warning(bstack111111l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡺࡪࡸࡳࡪࡱࡱࠤ࡬ࡸࡥࡢࡶࡨࡶࠥࡺࡨࡢࡰࠣࠦᒮ") + str(bstack1l1111l1ll1_opy_) + bstack111111l_opy_ (u"ࠥ࠲ࠧᒯ"))
                return False
            bstack1l111ll11ll_opy_ = caps.get(bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᒰ"), {}).get(bstack111111l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᒱ"))
            if not bstack1l111ll11ll_opy_:
                bstack1l111ll11ll_opy_ = caps.get(bstack111111l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᒲ"), {})
            if bstack1l111ll11ll_opy_ and bstack111111l_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫᒳ") in bstack1l111ll11ll_opy_.get(bstack111111l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ᒴ"), []):
                self.logger.warning(bstack111111l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦᒵ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧᒶ") + str(error))
            return False
    def bstack1l1111ll111_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111llll11_opy_ = {
            bstack111111l_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫᒷ"): test_uuid,
        }
        bstack1l1111lll1l_opy_ = {}
        if result.success:
            bstack1l1111lll1l_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l1ll1l_opy_(bstack1l111llll11_opy_, bstack1l1111lll1l_opy_)
    def bstack1lllllll1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1l1ll1ll_opy_ = None
        try:
            self.bstack1llll1l1ll1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack111111l_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧᒸ")
            req.script_name = bstack111111l_opy_ (u"ࠨࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠦᒹ")
            r = self.bstack111111111l_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack111111l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡧࡶ࡮ࡼࡥࡳࠢࡨࡼࡪࡩࡵࡵࡧࠣࡴࡦࡸࡡ࡮ࡵࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᒺ") + str(r.error) + bstack111111l_opy_ (u"ࠣࠤᒻ"))
            else:
                bstack1l111llll11_opy_ = self.bstack1l1111ll111_opy_(test_uuid, r)
                bstack1lll1ll1111_opy_ = r.script
            self.logger.debug(bstack111111l_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡧࡶࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠬᒼ") + str(bstack1l111llll11_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1ll1111_opy_:
                self.logger.debug(bstack111111l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᒽ") + str(framework_name) + bstack111111l_opy_ (u"ࠦࠥࠨᒾ"))
                return
            bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack1l111l1l111_opy_.value)
            self.bstack1l111ll1ll1_opy_(driver, bstack1lll1ll1111_opy_, bstack1l111llll11_opy_, framework_name)
            self.logger.info(bstack111111l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠣᒿ"))
            bstack1llllll1lll_opy_.end(EVENTS.bstack1l111l1l111_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᓀ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᓁ"), True, None, command=bstack111111l_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ᓂ"),test_name=name)
        except Exception as bstack1l111ll1l1l_opy_:
            self.logger.error(bstack111111l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦᓃ") + bstack111111l_opy_ (u"ࠥࡷࡹࡸࠨࡱࡣࡷ࡬࠮ࠨᓄ") + bstack111111l_opy_ (u"ࠦࠥࡋࡲࡳࡱࡵࠤ࠿ࠨᓅ") + str(bstack1l111ll1l1l_opy_))
            bstack1llllll1lll_opy_.end(EVENTS.bstack1l111l1l111_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᓆ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᓇ"), False, bstack1l111ll1l1l_opy_, command=bstack111111l_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬᓈ"),test_name=name)
    def bstack1l111ll1ll1_opy_(self, driver, bstack1lll1ll1111_opy_, bstack1l111llll11_opy_, framework_name):
        if framework_name == bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᓉ"):
            self.bstack1l11ll11lll_opy_.bstack1llll11l11l_opy_(driver, bstack1lll1ll1111_opy_, bstack1l111llll11_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1ll1111_opy_, bstack1l111llll11_opy_))
    def _1l111l1l1l1_opy_(self, instance: bstack1lll1lll1l1_opy_, args: Tuple) -> list:
        bstack111111l_opy_ (u"ࠤࠥࠦࡊࡾࡴࡳࡣࡦࡸࠥࡺࡡࡨࡵࠣࡦࡦࡹࡥࡥࠢࡲࡲࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠱ࠦࠧࠨᓊ")
        if bstack111111l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᓋ") in instance.bstack1ll11l11ll1_opy_:
            return args[2].tags if hasattr(args[2], bstack111111l_opy_ (u"ࠫࡹࡧࡧࡴࠩᓌ")) else []
        if hasattr(args[0], bstack111111l_opy_ (u"ࠬࡵࡷ࡯ࡡࡰࡥࡷࡱࡥࡳࡵࠪᓍ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111l1lll_opy_(self, tags, capabilities):
        return self.bstack11l11ll11l_opy_(tags) and self.bstack1l1l1ll11_opy_(capabilities)