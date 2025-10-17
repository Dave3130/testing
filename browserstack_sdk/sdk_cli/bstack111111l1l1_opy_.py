# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1111111lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1llll1l11ll_opy_,
    bstack1lll11l1ll1_opy_,
    bstack1llll1l1l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_, bstack1lll1l11l11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll111llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1l1_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1llll11llll_opy_
from bstack_utils.helper import bstack1l1111llll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack11l1ll11l_opy_ import bstack111111l11l_opy_
import grpc
import traceback
import json
class bstack1l1l11lll1l_opy_(bstack1lllll1l1l1_opy_):
    bstack1l1ll1l1l11_opy_ = False
    bstack1l111ll1111_opy_ = bstack11111_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࠨᐡ")
    bstack1l111l11l1l_opy_ = bstack11111_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦ࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶࠧᐢ")
    bstack1l111l1ll1l_opy_ = bstack11111_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢ࡭ࡳ࡯ࡴࠣᐣ")
    bstack1l1111ll1ll_opy_ = bstack11111_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣ࡮ࡹ࡟ࡴࡥࡤࡲࡳ࡯࡮ࡨࠤᐤ")
    bstack1l111l111l1_opy_ = bstack11111_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶࡤ࡮ࡡࡴࡡࡸࡶࡱࠨᐥ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l1l11l1l_opy_, bstack1ll1lll1l11_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111lll111_opy_ = False
        self.bstack1l111ll111l_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11ll1l11l_opy_ = bstack1ll1lll1l11_opy_
        bstack1l1l1l11l1l_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll1lll_opy_, bstack1llll1l11ll_opy_.PRE), self.bstack1l1111l1ll1_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.PRE), self.bstack1llll11l1ll_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111lllll_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1llll111l1l_opy_)
        if self.bstack1l111lll111_opy_:
            self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩࠨᐦ")] = f.get_state(instance, TestFramework.bstack1lll11lllll_opy_)
        if bstack11111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᐧ") in instance.bstack1ll111llll1_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1lllll1111l_opy_)
            self.accessibility = self.bstack1l1111ll1l1_opy_(tags, self.config[bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᐨ")][platform_index])
        else:
            capabilities = self.bstack1l11ll1l11l_opy_.bstack1lll1l1llll_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᐩ") + str(kwargs) + bstack11111_opy_ (u"ࠥࠦᐪ"))
                return
            self.accessibility = self.bstack1l1111ll1l1_opy_(tags, capabilities)
        if self.bstack1l11ll1l11l_opy_.pages and self.bstack1l11ll1l11l_opy_.pages.values():
            bstack1l111ll11l1_opy_ = list(self.bstack1l11ll1l11l_opy_.pages.values())
            if bstack1l111ll11l1_opy_ and isinstance(bstack1l111ll11l1_opy_[0], (list, tuple)) and bstack1l111ll11l1_opy_[0]:
                bstack1l111l1lll1_opy_ = bstack1l111ll11l1_opy_[0][0]
                if callable(bstack1l111l1lll1_opy_):
                    page = bstack1l111l1lll1_opy_()
                    def bstack1111ll11l_opy_():
                        self.get_accessibility_results(page, bstack11111_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᐫ"))
                    def bstack1l1111l1lll_opy_():
                        self.get_accessibility_results_summary(page, bstack11111_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᐬ"))
                    setattr(page, bstack11111_opy_ (u"ࠨࡧࡦࡶࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡔࡨࡷࡺࡲࡴࡴࠤᐭ"), bstack1111ll11l_opy_)
                    setattr(page, bstack11111_opy_ (u"ࠢࡨࡧࡷࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡕࡩࡸࡻ࡬ࡵࡕࡸࡱࡲࡧࡲࡺࠤᐮ"), bstack1l1111l1lll_opy_)
        self.logger.debug(bstack11111_opy_ (u"ࠣࡵ࡫ࡳࡺࡲࡤࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡼࡡ࡭ࡷࡨࡁࠧᐯ") + str(self.accessibility) + bstack11111_opy_ (u"ࠤࠥᐰ"))
    def bstack1l1111l1ll1_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1lll11l111_opy_ = datetime.now()
            self.bstack1l1111lll1l_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻࡫ࡱ࡭ࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᐱ"), datetime.now() - bstack1lll11l111_opy_)
            if (
                not f.bstack1l1lll11lll_opy_(method_name)
                or f.bstack1l1llll111l_opy_(method_name, *args)
                or f.bstack1l1lll11ll1_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l11lll1l_opy_.bstack1l111l1ll1l_opy_, False):
                if not bstack1l1l11lll1l_opy_.bstack1l1ll1l1l11_opy_:
                    self.logger.warning(bstack11111_opy_ (u"ࠦࡠࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢᐲ") + str(f.platform_index) + bstack11111_opy_ (u"ࠧࡣࠠࡢ࠳࠴ࡽࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡭ࡧࡶࡦࠢࡱࡳࡹࠦࡢࡦࡧࡱࠤࡸ࡫ࡴࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡷࡪࡹࡳࡪࡱࡱࠦᐳ"))
                    bstack1l1l11lll1l_opy_.bstack1l1ll1l1l11_opy_ = True
                return
            bstack1l111ll1lll_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111ll1lll_opy_:
                platform_index = f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_, 0)
                self.logger.debug(bstack11111_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᐴ") + str(f.framework_name) + bstack11111_opy_ (u"ࠢࠣᐵ"))
                return
            command_name = f.bstack1l1lll11l11_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11111_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࠥᐶ") + str(method_name) + bstack11111_opy_ (u"ࠤࠥᐷ"))
                return
            bstack1l1111l1l1l_opy_ = f.get_state(instance, bstack1l1l11lll1l_opy_.bstack1l111l111l1_opy_, False)
            if command_name == bstack11111_opy_ (u"ࠥ࡫ࡪࡺࠢᐸ") and not bstack1l1111l1l1l_opy_:
                f.bstack11111111ll_opy_(instance, bstack1l1l11lll1l_opy_.bstack1l111l111l1_opy_, True)
                bstack1l1111l1l1l_opy_ = True
            if not bstack1l1111l1l1l_opy_ and not self.bstack1l111lll111_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠦࡳࡵࠠࡖࡔࡏࠤࡱࡵࡡࡥࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᐹ") + str(command_name) + bstack11111_opy_ (u"ࠧࠨᐺ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11111_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦᐻ") + str(command_name) + bstack11111_opy_ (u"ࠢࠣᐼ"))
                return
            self.logger.info(bstack11111_opy_ (u"ࠣࡴࡸࡲࡳ࡯࡮ࡨࠢࡾࡰࡪࡴࠨࡴࡥࡵ࡭ࡵࡺࡳࡠࡶࡲࡣࡷࡻ࡮ࠪࡿࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᐽ") + str(command_name) + bstack11111_opy_ (u"ࠤࠥᐾ"))
            scripts = [(s, bstack1l111ll1lll_opy_[s]) for s in scripts_to_run if s in bstack1l111ll1lll_opy_]
            for script_name, bstack1lll1lll1l1_opy_ in scripts:
                try:
                    bstack1lll11l111_opy_ = datetime.now()
                    if script_name == bstack11111_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᐿ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࠥᑀ") + script_name, datetime.now() - bstack1lll11l111_opy_)
                    if isinstance(result, dict) and not result.get(bstack11111_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨᑁ"), True):
                        self.logger.warning(bstack11111_opy_ (u"ࠨࡳ࡬࡫ࡳࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡳࡧࡰࡥ࡮ࡴࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡶ࠾ࠥࠨᑂ") + str(result) + bstack11111_opy_ (u"ࠢࠣᑃ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11111_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡀࡿࡸࡩࡲࡪࡲࡷࡣࡳࡧ࡭ࡦࡿࠣࡩࡷࡸ࡯ࡳ࠿ࠥᑄ") + str(e) + bstack11111_opy_ (u"ࠤࠥᑅ"))
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡦࡴࡵࡳࡷࡃࠢᑆ") + str(e) + bstack11111_opy_ (u"ࠦࠧᑇ"))
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111lllll_opy_(instance, args)
        capabilities = self.bstack1l11ll1l11l_opy_.bstack1lll1l1llll_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111ll1l1_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᑈ"))
            return
        driver = self.bstack1l11ll1l11l_opy_.bstack1lll1llll1l_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll111ll1l1_opy_)
        if not test_name:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᑉ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll11lllll_opy_)
        if not test_uuid:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧᑊ"))
            return
        if isinstance(self.bstack1l11ll1l11l_opy_, bstack1lll1l1111l_opy_):
            framework_name = bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᑋ")
        else:
            framework_name = bstack11111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫᑌ")
        self.bstack1llll1l1l_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1l1lllll1ll_opy_ = bstack111111l11l_opy_.bstack1ll1l11l1l1_opy_(EVENTS.bstack1l1l11l1l1_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࠦᑍ"))
            return
        bstack1lll11l111_opy_ = datetime.now()
        bstack1lll1lll1l1_opy_ = self.scripts.get(framework_name, {}).get(bstack11111_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᑎ"), None)
        if not bstack1lll1lll1l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡥࡤࡲࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᑏ") + str(framework_name) + bstack11111_opy_ (u"ࠨࠠࠣᑐ"))
            return
        if self.bstack1l111lll111_opy_:
            arg = dict()
            arg[bstack11111_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᑑ")] = method if method else bstack11111_opy_ (u"ࠣࠤᑒ")
            arg[bstack11111_opy_ (u"ࠤࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠤᑓ")] = self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᑔ")]
            arg[bstack11111_opy_ (u"ࠦࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠤᑕ")] = self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠥᑖ")]
            arg[bstack11111_opy_ (u"ࠨࡡࡶࡶ࡫ࡌࡪࡧࡤࡦࡴࠥᑗ")] = self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠧᑘ")]
            arg[bstack11111_opy_ (u"ࠣࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠧᑙ")] = self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠤࡷ࡬ࡤࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠣᑚ")]
            arg[bstack11111_opy_ (u"ࠥࡷࡨࡧ࡮ࡕ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠥᑛ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111l1l1l1_opy_ = bstack1lll1lll1l1_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l1l1l1_opy_)
            return
        instance = bstack1lll11l1ll1_opy_.bstack1ll1ll1111l_opy_(driver)
        if instance:
            if not bstack1lll11l1ll1_opy_.get_state(instance, bstack1l1l11lll1l_opy_.bstack1l1111ll1ll_opy_, False):
                bstack1lll11l1ll1_opy_.bstack11111111ll_opy_(instance, bstack1l1l11lll1l_opy_.bstack1l1111ll1ll_opy_, True)
            else:
                self.logger.info(bstack11111_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡯࡮ࠡࡲࡵࡳ࡬ࡸࡥࡴࡵࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࠽ࠣᑜ") + str(method) + bstack11111_opy_ (u"ࠧࠨᑝ"))
                return
        self.logger.info(bstack11111_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡀࠦᑞ") + str(method) + bstack11111_opy_ (u"ࠢࠣᑟ"))
        if framework_name == bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᑠ"):
            result = self.bstack1l11ll1l11l_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll1lll1l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll1l1_opy_, {bstack11111_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤᑡ"): method if method else bstack11111_opy_ (u"ࠥࠦᑢ")})
        bstack111111l11l_opy_.end(EVENTS.bstack1l1l11l1l1_opy_.value, bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᑣ"), bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᑤ"), True, None, command=method)
        if instance:
            bstack1lll11l1ll1_opy_.bstack11111111ll_opy_(instance, bstack1l1l11lll1l_opy_.bstack1l1111ll1ll_opy_, False)
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾ࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰࠥᑥ"), datetime.now() - bstack1lll11l111_opy_)
        return result
        def bstack1l111l111ll_opy_(self, driver: object, framework_name, bstack11ll1111ll_opy_: str):
            self.bstack1lllll1lll1_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111ll11l_opy_ = self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠢᑦ")]
            req.bstack11ll1111ll_opy_ = bstack11ll1111ll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llll1lll11_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11111_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᑧ") + str(r) + bstack11111_opy_ (u"ࠤࠥᑨ"))
                else:
                    bstack1l111l1111l_opy_ = json.loads(r.bstack1l111ll11ll_opy_.decode(bstack11111_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᑩ")))
                    if bstack11ll1111ll_opy_ == bstack11111_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨᑪ"):
                        return bstack1l111l1111l_opy_.get(bstack11111_opy_ (u"ࠧࡪࡡࡵࡣࠥᑫ"), [])
                    else:
                        return bstack1l111l1111l_opy_.get(bstack11111_opy_ (u"ࠨࡤࡢࡶࡤࠦᑬ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡳࡴࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࠥ࡬ࡲࡰ࡯ࠣࡧࡱ࡯࠺ࠡࠤᑭ") + str(e) + bstack11111_opy_ (u"ࠣࠤᑮ"))
    @measure(event_name=EVENTS.bstack11l1lll11_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᑯ"))
            return
        if self.bstack1l111lll111_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡤࡴࡵࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᑰ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l111ll_opy_(driver, framework_name, bstack11111_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠣᑱ"))
        bstack1lll1lll1l1_opy_ = self.scripts.get(framework_name, {}).get(bstack11111_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤᑲ"), None)
        if not bstack1lll1lll1l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᑳ") + str(framework_name) + bstack11111_opy_ (u"ࠢࠣᑴ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1lll11l111_opy_ = datetime.now()
        if framework_name == bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᑵ"):
            result = self.bstack1l11ll1l11l_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll1lll1l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll1l1_opy_)
        instance = bstack1lll11l1ll1_opy_.bstack1ll1ll1111l_opy_(driver)
        if instance:
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠧᑶ"), datetime.now() - bstack1lll11l111_opy_)
        return result
    @measure(event_name=EVENTS.bstack111ll11ll1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࡠࡵࡸࡱࡲࡧࡲࡺ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᑷ"))
            return
        if self.bstack1l111lll111_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l111ll_opy_(driver, framework_name, bstack11111_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨᑸ"))
        bstack1lll1lll1l1_opy_ = self.scripts.get(framework_name, {}).get(bstack11111_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠤᑹ"), None)
        if not bstack1lll1lll1l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᑺ") + str(framework_name) + bstack11111_opy_ (u"ࠢࠣᑻ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1lll11l111_opy_ = datetime.now()
        if framework_name == bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᑼ"):
            result = self.bstack1l11ll1l11l_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll1lll1l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll1l1_opy_)
        instance = bstack1lll11l1ll1_opy_.bstack1ll1ll1111l_opy_(driver)
        if instance:
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࡤࡹࡵ࡮࡯ࡤࡶࡾࠨᑽ"), datetime.now() - bstack1lll11l111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111llll11_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l111lll1ll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llll1lll11_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᑾ") + str(r) + bstack11111_opy_ (u"ࠦࠧᑿ"))
            else:
                self.bstack1l111l1ll11_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᒀ") + str(e) + bstack11111_opy_ (u"ࠨࠢᒁ"))
            traceback.print_exc()
            raise e
    def bstack1l111l1ll11_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11111_opy_ (u"ࠢ࡭ࡱࡤࡨࡤࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢᒂ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111lll111_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠣࡶࡨࡷࡹ࡮ࡵࡣࡡࡥࡹ࡮ࡲࡤࡠࡷࡸ࡭ࡩࠨᒃ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111ll111l_opy_[bstack11111_opy_ (u"ࠤࡷ࡬ࡤࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠣᒄ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111ll111l_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111ll1l1l_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111ll1111_opy_ and command.module == self.bstack1l111l11l1l_opy_:
                        if command.method and not command.method in bstack1l111ll1l1l_opy_:
                            bstack1l111ll1l1l_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111ll1l1l_opy_[command.method]:
                            bstack1l111ll1l1l_opy_[command.method][command.name] = list()
                        bstack1l111ll1l1l_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111ll1l1l_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l1111lll1l_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11ll1l11l_opy_, bstack1lll1l1111l_opy_) and method_name != bstack11111_opy_ (u"ࠪࡧࡴࡴ࡮ࡦࡥࡷࠫᒅ"):
            return
        if bstack1lll11l1ll1_opy_.bstack1llllllll1l_opy_(instance, bstack1l1l11lll1l_opy_.bstack1l111l1ll1l_opy_):
            return
        if f.bstack1lllll1l11l_opy_(method_name, *args):
            bstack1l111ll1ll1_opy_ = False
            desired_capabilities = f.bstack1l1ll1lll1l_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll1l1l1_opy_(instance)
                platform_index = f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_, 0)
                bstack1l111ll1l11_opy_ = datetime.now()
                r = self.bstack1l111lll1ll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡦࡳࡳ࡬ࡩࡨࠤᒆ"), datetime.now() - bstack1l111ll1l11_opy_)
                bstack1l111ll1ll1_opy_ = r.success
            else:
                self.logger.error(bstack11111_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡤࡦࡵ࡬ࡶࡪࡪࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࡃࠢᒇ") + str(desired_capabilities) + bstack11111_opy_ (u"ࠨࠢᒈ"))
            f.bstack11111111ll_opy_(instance, bstack1l1l11lll1l_opy_.bstack1l111l1ll1l_opy_, bstack1l111ll1ll1_opy_)
    def bstack11l1lllll_opy_(self, test_tags):
        bstack1l111lll1ll_opy_ = self.config.get(bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᒉ"))
        if not bstack1l111lll1ll_opy_:
            return True
        try:
            include_tags = bstack1l111lll1ll_opy_[bstack11111_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒊ")] if bstack11111_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒋ") in bstack1l111lll1ll_opy_ and isinstance(bstack1l111lll1ll_opy_[bstack11111_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒌ")], list) else []
            exclude_tags = bstack1l111lll1ll_opy_[bstack11111_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒍ")] if bstack11111_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒎ") in bstack1l111lll1ll_opy_ and isinstance(bstack1l111lll1ll_opy_[bstack11111_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒏ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢᒐ") + str(error))
        return False
    def bstack111l1l1ll_opy_(self, caps):
        try:
            if self.bstack1l111lll111_opy_:
                bstack1l111l1llll_opy_ = caps.get(bstack11111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢᒑ"))
                if bstack1l111l1llll_opy_ is not None and str(bstack1l111l1llll_opy_).lower() == bstack11111_opy_ (u"ࠤࡤࡲࡩࡸ࡯ࡪࡦࠥᒒ"):
                    bstack1l1111ll111_opy_ = caps.get(bstack11111_opy_ (u"ࠥࡥࡵࡶࡩࡶ࡯࠽ࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧᒓ")) or caps.get(bstack11111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨᒔ"))
                    if bstack1l1111ll111_opy_ is not None and int(bstack1l1111ll111_opy_) < 11:
                        self.logger.warning(bstack11111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡇ࡮ࡥࡴࡲ࡭ࡩࠦ࠱࠲ࠢࡤࡲࡩࠦࡡࡣࡱࡹࡩ࠳ࠦࡃࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡹࡩࡷࡹࡩࡰࡰࠣࡁࠧᒕ") + str(bstack1l1111ll111_opy_) + bstack11111_opy_ (u"ࠨࠢᒖ"))
                        return False
                return True
            bstack1l111l11l11_opy_ = caps.get(bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᒗ"), {}).get(bstack11111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᒘ"), caps.get(bstack11111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩᒙ"), bstack11111_opy_ (u"ࠪࠫᒚ")))
            if bstack1l111l11l11_opy_:
                self.logger.warning(bstack11111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᒛ"))
                return False
            browser = caps.get(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᒜ"), bstack11111_opy_ (u"࠭ࠧᒝ")).lower()
            if browser != bstack11111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧᒞ"):
                self.logger.warning(bstack11111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᒟ"))
                return False
            bstack1l111lll11l_opy_ = bstack1l111lll1l1_opy_
            if not self.config.get(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᒠ")) or self.config.get(bstack11111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᒡ")):
                bstack1l111lll11l_opy_ = bstack1l111l1l11l_opy_
            browser_version = caps.get(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᒢ"))
            if not browser_version:
                browser_version = caps.get(bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᒣ"), {}).get(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᒤ"), bstack11111_opy_ (u"ࠧࠨᒥ"))
            if browser_version and browser_version != bstack11111_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨᒦ") and int(browser_version.split(bstack11111_opy_ (u"ࠩ࠱ࠫᒧ"))[0]) <= bstack1l111lll11l_opy_:
                self.logger.warning(bstack11111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤࠧᒨ") + str(bstack1l111lll11l_opy_) + bstack11111_opy_ (u"ࠦ࠳ࠨᒩ"))
                return False
            bstack1l111l11ll1_opy_ = caps.get(bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᒪ"), {}).get(bstack11111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᒫ"))
            if not bstack1l111l11ll1_opy_:
                bstack1l111l11ll1_opy_ = caps.get(bstack11111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᒬ"), {})
            if bstack1l111l11ll1_opy_ and bstack11111_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬᒭ") in bstack1l111l11ll1_opy_.get(bstack11111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧᒮ"), []):
                self.logger.warning(bstack11111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧᒯ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨᒰ") + str(error))
            return False
    def bstack1l111llll1l_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l11lll_opy_ = {
            bstack11111_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬᒱ"): test_uuid,
        }
        bstack1l1111lll11_opy_ = {}
        if result.success:
            bstack1l1111lll11_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l1111llll1_opy_(bstack1l111l11lll_opy_, bstack1l1111lll11_opy_)
    def bstack1llll1l1l_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1l1lllll1ll_opy_ = None
        try:
            self.bstack1lllll1lll1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11111_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠨᒲ")
            req.script_name = bstack11111_opy_ (u"ࠢࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒳ")
            r = self.bstack1llll1lll11_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡨࡷ࡯ࡶࡦࡴࠣࡩࡽ࡫ࡣࡶࡶࡨࠤࡵࡧࡲࡢ࡯ࡶࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᒴ") + str(r.error) + bstack11111_opy_ (u"ࠤࠥᒵ"))
            else:
                bstack1l111l11lll_opy_ = self.bstack1l111llll1l_opy_(test_uuid, r)
                bstack1lll1lll1l1_opy_ = r.script
            self.logger.debug(bstack11111_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡡࡷ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ᒶ") + str(bstack1l111l11lll_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1lll1l1_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᒷ") + str(framework_name) + bstack11111_opy_ (u"ࠧࠦࠢᒸ"))
                return
            bstack1l1lllll1ll_opy_ = bstack111111l11l_opy_.bstack1ll1l11l1l1_opy_(EVENTS.bstack1l111l1l111_opy_.value)
            self.bstack1l111l1l1ll_opy_(driver, bstack1lll1lll1l1_opy_, bstack1l111l11lll_opy_, framework_name)
            self.logger.info(bstack11111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠤᒹ"))
            bstack111111l11l_opy_.end(EVENTS.bstack1l111l1l111_opy_.value, bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᒺ"), bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᒻ"), True, None, command=bstack11111_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᒼ"),test_name=name)
        except Exception as bstack1l111l11111_opy_:
            self.logger.error(bstack11111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧᒽ") + bstack11111_opy_ (u"ࠦࡸࡺࡲࠩࡲࡤࡸ࡭࠯ࠢᒾ") + bstack11111_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢᒿ") + str(bstack1l111l11111_opy_))
            bstack111111l11l_opy_.end(EVENTS.bstack1l111l1l111_opy_.value, bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᓀ"), bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᓁ"), False, bstack1l111l11111_opy_, command=bstack11111_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ᓂ"),test_name=name)
    def bstack1l111l1l1ll_opy_(self, driver, bstack1lll1lll1l1_opy_, bstack1l111l11lll_opy_, framework_name):
        if framework_name == bstack11111_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᓃ"):
            self.bstack1l11ll1l11l_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll1lll1l1_opy_, bstack1l111l11lll_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1lll1l1_opy_, bstack1l111l11lll_opy_))
    def _1l1111lllll_opy_(self, instance: bstack1lll1l11l11_opy_, args: Tuple) -> list:
        bstack11111_opy_ (u"ࠥࠦࠧࡋࡸࡵࡴࡤࡧࡹࠦࡴࡢࡩࡶࠤࡧࡧࡳࡦࡦࠣࡳࡳࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠲ࠧࠨࠢᓄ")
        if bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᓅ") in instance.bstack1ll111llll1_opy_:
            return args[2].tags if hasattr(args[2], bstack11111_opy_ (u"ࠬࡺࡡࡨࡵࠪᓆ")) else []
        if hasattr(args[0], bstack11111_opy_ (u"࠭࡯ࡸࡰࡢࡱࡦࡸ࡫ࡦࡴࡶࠫᓇ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111ll1l1_opy_(self, tags, capabilities):
        return self.bstack11l1lllll_opy_(tags) and self.bstack111l1l1ll_opy_(capabilities)